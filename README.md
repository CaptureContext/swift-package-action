<p align="center">
  <img src=".media/swiftpm.png" alt="swift-package-action logo" height=300px/>
</p>

<h1 align="center">
  swift-package-action
</h1>
<h5 align="center">
  Set of predefined commands for multiplatform Swift packages.
</h5>

<p align="center" style="padding: 0 80px;">
    <i>If you develop a bunch swift packages it may be tricky to keep CI clean and updated for all of them, but a dedicated action can reduce code duplication and simplify CI support. This repository was inspired by CI setup of <a href="https://github.com/pointfreeco/swift-composable-architecture">The Composable Architecture</a>.</i>
</p>




## Getting started 🚀

You can include the action in your workflow to trigger on any event that [GitHub actions supports](https://help.github.com/en/articles/events-that-trigger-workflows).

The `with` portion of the workflow **must** be configured for the action.

</br>

### ⌘ `with.command`

_Command for the action, basically it's the name of `MAKE` workflow. For additional details check out [Makefile](Makefile)_

**Type:** `required`

**Supported values:**

- `xcodebuild`
- `xcodebuild-raw`
- `build-for-library-evolution`
- `test-docs`
  - [_`unchecked`_, _`experimental`_] for @2.0, please submit an issue if you face any
- `benchmark`
  - [_`unchecked`_, _`experimental`_] for @2.0, please submit an issue if you face any
- `github-build-docs`
  - [_`unchecked`_, _`experimental`_] for @2.0, please submit an issue if you face any
- `swift-format`
  - [_`unchecked`_] for @2.0, but should work fine
  - _Requires GitHub Secrets to be set up for committing changes_
  - _Uses [swift-format](https://github.com/swiftlang/swift-format)_
  - _Commits changes to_ `main` _branch, this behavior is not configurable, at least yet_
  - _Commit message is_ `[swift-format]` _and is not configurable, at least yet_

> [!NOTE]
> _Commands with `unchecked` and `experimental` tags is in todo for verification. These flags mean that at some point these commands were used locally, but their use on CI was not validated. Currently we're in the process of migrating our repos to this action, but not every package uses these commands, however any potential issues for those commands should be fixed soon._
</br>

### ⌘ `with.subcommand`

_Subcommand for the action, basically only used as argument for `xcodebuild`/`xcodebuild-raw` commands_

**Type:** `optional`

**Default value:** `''`

**Supported values:**

- `''`
- `test`
- _any other xcodebuild argument_

</br>

### ⌘ `with.xcode`

_Xcode version_

**Type:** `optional`

**Default value:** `16.2`

</br>

### ⌘ `with.cache-derived-data`

_Argument that specifies if action should cache DerivedData_

**Type:** `optional`

**Default value:** `false`

**Supported values:**

- `false`
- `true`

</br>

### ⌘ `with.workspace`

_Path to xcworkspace. It is recommended to create a workspace at the root of the package and ensure that all required schemes are present._

**Type:** `optional`

**Default value:** `.swiftpm/xcode/package.xcworkspace`

</br>

### ⌘ `with.scheme`

_Scheme/PackageTarget for the action._

>  `<package-name>-package` _usually suits for building and for testing_

**Type:**

- **`required`**
- **`optional`** for `swift-format` command

</br>

### ⌘ `with.platform`

_Target platform for the action_

**Type:**

- **`optional`**
- **`required`** for the following commands
  - `xcodebuild`
  - `xcodebuild-raw`
  - `test-docs`

**Supported values:**

- `iOS`
- `macOS`
- `macCatalyst`
- `watchOS`
- `tvOS`
- `visionOS`

</br>

### ⌘ `with.config`

_Build configuration for the action._

**Type:** `optional`

**Default value:** `Debug`

</br>

### ⌘ `with.beautify`

_Specifies if xcodebuild output should be beautified. Uses [`xcbeautify`](https://github.com/cpisciotta/xcbeautify)_

**Type:** `optional`

**Default value:** `quiet`

**Supported values:**

- `quiet`
- `true`
- `false`

</br>

### ⌘ `with.working-directory`

_Relative path to target directory_

**Type:** `optional`

**Default value:** `'.'`

</br>

### 🧩 Step examples:

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

#### Short:

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



### 📚 Workflow examples

- [**`swift-existential-container`**](https://github.com/capturecontext/swift-existential-container/blob/main/.github/workflows/ci.yml)
- `swift-composable-architecture`
  - **_[Original](https://github.com/pointfreeco/swift-composable-architecture/blob/main/.github/workflows/ci.yml)_**
  - **_[SwiftPackageAction](https://github.com/capturecontext/swift-composable-architecture-ci-explorations/blob/main/.github/workflows/ci.yml)_**


## License 🪪

This action is released under the MIT license. See [LICENSE](LICENSE) for details.

See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md) for inspiration references and their licences.
