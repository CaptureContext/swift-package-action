<p align="center">
  <img src=".media/swiftpm.png" alt="swift-package-action logo" height=300px/>
</p>

<h1 align="center">
  swift-package-action
</h1>
<p align="center" style="font-size: 18px;">
  <span style="color:#808080;">
    Set of predefined commands for multiplatform Swift packages.
  </span>
</p>

<p align="center" style="padding: 0 80px;">
  <span style="color:#808080CC;">
      This repository was inspired by <a href="https://github.com/pointfreeco/swift-composable-architecture">The Composable Architecture</a>. If you develop a bunch swift packages it may be tricky to keep CI clean and updated for all of them, but a dedicated action can reduce code duplication and simplify CI support.
  </span>
</p>




## Getting started ✈️

You can include the action in your workflow to trigger on any event that [GitHub actions supports](https://help.github.com/en/articles/events-that-trigger-workflows).

The `with` portion of the workflow **must** be configured for the action.



### `with.command`

Command for the action, basically it's the name of `MAKE` workflow. For additional details check out [Makefile](Makefile)

##### Type: `required`

##### Supported values:

- `xcodebuild`
- `xcodebuild-raw`
- `build-for-library-evolution`
- `test-docs`
- `benchmark`
- `github-build-docs`
- `swift-format`
  - _Requires GitHub Secrets to be set up for committing changes_
  - _Uses [swift-format](https://github.com/swiftlang/swift-format)_
  - _Commits changes to_ `main` _branch, this behavior is not configurable, at least yet_
  - _Commit message is_ `[swift-format]` _and is not configurable, at least yet_

### `with.subcommand`

Subcommand for the action, basically only used as argument for `xcodebuild`/`xcodebuild-raw` commands

##### Type: `optional`

##### Default value: `''`

##### Supported values:

- `''`
- `test`
- _any other xcodebuild argument_



### `with.xcode`

Xcode version

##### Type: `optional`

##### Default value: `16.2`



### `with.cache-derived-data`

Argument that specifies if action should cache DerivedData

##### Type: `optional`

##### Default value: `false`

##### Supported values:

- `false`
- `true`



### `with.workspace`

Path to xcworkspace. It is recommended to create a workspace at the root of the package and ensure that all required schemes are present.

##### Type: `optional`

##### Default value: `.swiftpm/xcode/package.xcworkspace`



### `with.scheme`

Scheme/PackageTarget for the action.

>  `<package-name>-package` _usually suits for building and for testing_

##### Type:

- **`required`**
- **`optional`** for `swift-format` command



### `with.platform`

Target platform for the action

##### Type:

- **`optional`**
- **`required`** for the following commands
  - `xcodebuild`
  - `xcodebuild-raw`
  - `test-docs`

##### Supported values:

- `iOS`
- `macOS`
- `macCatalyst`
- `watchOS`
- `tvOS`
- `visionOS`



### `with.config`

Build configuration for the action.

##### Type: `optional`

##### Default value: `Debug`



### `with.beautify`

Specifies if xcodebuild output should be beautified. Uses [`xcbeautify`](https://github.com/cpisciotta/xcbeautify)

##### Type: `optional`

##### Default value: `quiet`

##### Supported values:

- `quiet`
- `true`
- `false`



### `with.working-directory`

Relative path to target directory

##### Type: `optional`

##### Default value: `'.'`



### Step examples:

#### Full:


```yaml
- name: Test CoolStuff
  uses: capturecontext/swift-package-action@2.0
  with:
    xcode: 16.2
    workspace: 'Package.xcworkspace' # custom workspace at the root of a repo
    cache-derived-data: true
    command: xcodebuild
    subcommand: test
    scheme: cool-stuff-package # likely to be a name of the package
    platform: iOS
    config: Debug
    beautify: true
    working-directory: '.'
```

##### Short:

```yaml
- name: Test CoolStuff
  uses: capturecontext/swift-package-action@2.0
  with:
    workspace: 'Package.xcworkspace'
    cache-derived-data: true
    command: xcodebuild
    subcommand: test
    scheme: cool-stuff-package
    platform: iOS
```



### Workflow examples

- **_[Original](https://github.com/pointfreeco/swift-composable-architecture/blob/main/.github/workflows/ci.yml)_**
- **_[SwiftPackageAction](https://github.com/capturecontext/swift-composable-architecture-ci-explorations/blob/main/.github/workflows/ci.yml)_**



## License

This action is released under the MIT license. See [LICENSE](LICENSE) for details.

See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md) for inspiration references and their licences.
