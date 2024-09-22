# swift-package-action

Predefined actions for swift packages

### Configuration

```yaml
- name: Test MyPackageTarget
  uses: capturecontext/swift-package-action@1.0
  with:
    # Command for the action. (Required)
    # Available commands:
    # - xcodebuild
    # - xcodebuild-macros
    # - xcodebuild-macros-plugin
    # - build-for-library-evolution
    # - test-docs
    # - test-example
    # - test-integration
    # - benchmark
    # - format
    # - loop-platforms
    command: loop-platforms

    # Subcommand for the action. (Optional)
    # Available subcommands:
    # - test
    # - ''
    #
    # Default: ''
    subcommand: test
  
    # Base scheme for the action. (Required)
    #
    # Suffixes like -"Tests"/-"MacrosTests"/-"MacrosPluginTests" 
    # are added automatically for corresponding commands
    #
    # Schemes must be present in `.github/package.xcworkspace`
    scheme: MyPackageTarget

    # Platform for the action. (Required if used by action, ignored otherwise)
    # Values: [iOS, macOS, tvOS, watchOS, visionOS, macCatalyst]
    platform: iOS

    # Config to change to before for the action. (Optional)
    # Default: 'Debug'
    config: Debug

    # Directory to change to before running the action. (Optional)
    # Default: '.'
    working-directory: '.'

    # Platforms for `loop-platforms` make action (Required for `loop-platforms`)
    # Values: [iOS, macOS, tvOS, watchOS, visionOS, macCatalyst]
    platforms: iOS,macOS,watchOS

    # Command to be executed on different platforms using `loop-platforms` action
    # (Required for `loop-platforms`)
    # Available commands:
    # - xcodebuild
    # - xcodebuild-macros
    # - xcodebuild-macros-plugin
    # - build-for-library-evolution
    # - test-docs
    # - test-example
    # - test-integration
    # - benchmark
    # - format
    target: xcodebuild
```

### Example

- _[Example](https://github.com/capturecontext/swift-interception/blob/main/.github/workflows/ci.yml)_

```yaml
name: CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - '*'
  workflow_dispatch:

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true

jobs:
  test-library:
    name: test-library
    if: |
      !contains(github.event.head_commit.message, '[ci skip]') &&
      !contains(github.event.head_commit.message, '[ci skip test]') &&
      !contains(github.event.head_commit.message, '[ci skip library-swift-latest]')
    runs-on: macos-14
    strategy:
      matrix:
        scheme: [Interception]
        command: [test]
        platform: [iOS, macOS, tvOS, watchOS, macCatalyst]
        xcode: [15.4, '16.0']
        config: [Debug, Release]
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: true
      - name: Select Xcode ${{ matrix.xcode }}
        run: sudo xcode-select -s /Applications/Xcode_${{ matrix.xcode }}.app
      - name: Cache derived data
        uses: actions/cache@v3
        with:
          path: |
            ~/.derivedData
          key: |
            deriveddata-xcodebuild-${{ matrix.platform }}-${{ matrix.xcode }}-${{ matrix.command }}-${{ hashFiles('**/Sources/**/*.swift', '**/Tests/**/*.swift') }}
          restore-keys: |
            deriveddata-xcodebuild-${{ matrix.platform }}-${{ matrix.xcode }}-${{ matrix.command }}-
      - name: Set IgnoreFileSystemDeviceInodeChanges flag 
        run: defaults write com.apple.dt.XCBuild IgnoreFileSystemDeviceInodeChanges -bool YES
      - name: Update mtime for incremental builds 
        uses: chetan/git-restore-mtime-action@v2
      - name: test-library (${{ matrix.config }})
        uses: capturecontext/swift-package-action@1.0
        with:
          command: xcodebuild
          subcommand: ${{ matrix.command }}
          platform: ${{ matrix.platform }}
          scheme: ${{ matrix.scheme }}
          config: ${{ matrix.config }}
      - name: test-library-macros (${{ matrix.config }})
        uses: capturecontext/swift-package-action@1.0
        with:
          command: xcodebuild-macros
          subcommand: ${{ matrix.command }}
          platform: ${{ matrix.platform }}
          scheme: ${{ matrix.scheme }}
          config: ${{ matrix.config }}
  test-library-macros-plugin:
    name: test-library-macros-plugin
    if: |
      !contains(github.event.head_commit.message, '[ci skip]') &&
      !contains(github.event.head_commit.message, '[ci skip test]') &&
      !contains(github.event.head_commit.message, '[ci skip library-swift-latest]')
    runs-on: macos-14
    strategy:
      matrix:
        scheme: [Interception]
        command: [test]
        platform: [macOS]
        xcode: ['16.0']
        config: [Debug]
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: true
      - name: Select Xcode ${{ matrix.xcode }}
        run: sudo xcode-select -s /Applications/Xcode_${{ matrix.xcode }}.app
      - name: Cache derived data
        uses: actions/cache@v3
        with:
          path: |
            ~/.derivedData
          key: |
            deriveddata-xcodebuild-${{ matrix.platform }}-${{ matrix.xcode }}-${{ matrix.command }}-${{ hashFiles('**/Sources/**/*.swift', '**/Tests/**/*.swift') }}
          restore-keys: |
            deriveddata-xcodebuild-${{ matrix.platform }}-${{ matrix.xcode }}-${{ matrix.command }}-
      - name: Set IgnoreFileSystemDeviceInodeChanges flag 
        run: defaults write com.apple.dt.XCBuild IgnoreFileSystemDeviceInodeChanges -bool YES
      - name: Update mtime for incremental builds 
        uses: chetan/git-restore-mtime-action@v2
      - name: test-library-macros-plugin (${{ matrix.config }})
        uses: capturecontext/swift-package-action@1.0
        with:
          command: xcodebuild-macros-plugin
          subcommand: ${{ matrix.command }}
          platform: ${{ matrix.platform }}
          scheme: ${{ matrix.scheme }}
          config: ${{ matrix.config }}
```

