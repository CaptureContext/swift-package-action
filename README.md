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

**Type:** 

- `required`
- `optional` if you just want to cache derived data

**Supported values:**

- `xcodebuild`
- `xcodebuild-raw`
- `build-for-library-evolution`
- `test-docs`
  - [_`unchecked`_, _`experimental`_] for @2.0, please submit an issue if you face any
- `benchmark`
  - [_`unchecked`_, _`experimental`_] for @2.0, please submit an issue if you face any
- `cache-derived-data`
  - _Not a make command. Just a flag for [action.yml](action.yml)_
  - _See `with.cache-derived-data` for more details_
  - [_`unchecked`_, _`experimental`_] for @2.0, please submit an issue if you face any
- `github-build-docs`
  - [_`unchecked`_, _`experimental`_] for @2.0, please submit an issue if you face any
- `swift-format`
  - [_`unchecked`_] for @2.0, but should work fine
  - _Requires GitHub Secrets to be set up for committing changes_
  - _Uses [swift-format](https://github.com/swiftlang/swift-format)_
  - _Commit message can be specified with `with.swift-format-commit-message`_
  - _Commit branch can be specified with `with.swift-format-branch`_

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

> [!NOTE]
>
> _To skip `Select Xcode` step you can use set value to  `__unspecified__`_

</br>

### ⌘ `with.cache-derived-data`

_Argument that specifies if action should cache DerivedData, if you only want to cache derived data use `with.command: cache-derived-data`_

**Type:** `optional`

**Default value:** `false`

**Supported values:**

- `false`
- `true`

> [!NOTE]
>
> _Cache location is calculated based on_
>
> - `with.xcode`
> - `with.platform`
> - `with.subcommand`
> - _hash of the following files_
>   - `**/Sources/**/*.swift`
>   - `**/Tests/**/*.swift`  

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

  > [!WARNING]
  >
  > _This value will trigger `Install visionOS runtime` step. It will increase CI workflow duration and network usage_

**Default value:** `__unspecified__`

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

### ⌘ `with.swift-format-commit-message`

_Commit message for swift-format action_

**Type:** `optional`

**Default value:** `[swift-format]`

</br>

### ⌘ `with.swift-format-branch`

_Branch for committing result of swift-format action_

**Type:** `optional`

**Default value:** `main`

</br>

### 🧩 Step examples:

#### Full:


```yaml
- name: Test CoolStuff
  uses: capturecontext/swift-package-action@2.1
  with:
    xcode: 16.2
    workspace: Package.xcworkspace # custom workspace at the root of a repo
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
  uses: capturecontext/swift-package-action@2.1
  with:
    workspace: Package.xcworkspace
    cache-derived-data: true
    command: xcodebuild
    subcommand: test
    scheme: cool-stuff-package
    platform: iOS
```

#### Just cache derived data

```yaml
- name: Cache derived data
  uses: capturecontext/swift-package-action@2.1
  with:
    command: cache-derived-data
    xcode: 
```



### 📚 Workflow examples

- [**`swift-existential-container`**](https://github.com/capturecontext/swift-existential-container/blob/main/.github/workflows/ci.yml)
- `swift-composable-architecture`
  - **_[Original](https://github.com/pointfreeco/swift-composable-architecture/blob/main/.github/workflows/ci.yml)_**
  - **_[SwiftPackageAction](https://github.com/capturecontext/swift-composable-architecture-ci-explorations/blob/main/.github/workflows/ci.yml)_**


## License 🪪

This action is released under the MIT license. See [LICENSE](LICENSE) for details.

See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md) for inspiration references and their licences.
