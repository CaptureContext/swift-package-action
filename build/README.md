<p align="center">
  <img src="../.media/swiftpm.png" alt="swift-package-action logo" height=300px/>
</p>

<h1 align="center">
  swift-package-action/build
</h1>
<h5 align="center">
  Set of predefined commands for building multiplatform Swift packages.
</h5>


<p align="center" style="padding: 0 80px;">
    <i>If you develop a bunch swift packages it may be tricky to keep CI clean and updated for all of them, but a dedicated action can reduce code duplication and simplify CI support. This repository was inspired by CI setup of <a href="https://github.com/pointfreeco/swift-composable-architecture">The Composable Architecture</a>.</i>
</p>


## Getting started 🚀

You can include the action in your workflow to trigger on any event that [GitHub actions supports](https://help.github.com/en/articles/events-that-trigger-workflows).

The `with` portion of the workflow **must** be configured for the action.

</br>

### ⌘ `with.action`

_The name of `MAKE` workflow. For additional details check out [Makefile](Makefile)_

**Type:** 

- `required`
- `optional` if you just want to cache derived data

**Supported values:**

- `print-destination`
- `warm-simulator`
- `xcodebuild`
- `xcodebuild-test`
- `xcodebuild-raw`
- `xcodebuild-test-raw`
- `build-for-library-evolution`
- `benchmark`
  - [_`unchecked`_, _`experimental`_], please submit an issue if you face any
- `test-docs`
  - [_`unchecked`_, _`experimental`_], please submit an issue if you face any

> [!NOTE]
> _Commands with `unchecked` and `experimental` tags are in "todo" for verification. These flags mean that at some point these commands were used locally, but their use on CI was not validated. Currently we're in the process of migrating our repos to this action, but not every package uses these commands. However any potential issues for those commands should be fixed soon._

</br>

### ⌘ `with.xcode`

_Xcode version_

**Type:** `optional`

**Default value:** `26.2`

> [!NOTE]
>
> _To skip `Select Xcode` step you can explicitly set value to  `__unspecified__`_

</br>

### ⌘ `with.cache-derived-data`

_Argument that specifies if action should cache DerivedData, if you only want to cache derived data use `with.command: cache-derived-data`_ or a dedicated subaction `swift-package-action/cache/derived-data`

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
>
> You can also specify:
>
> - ⌘ `cache-derived-data-base-path` which is `~/.derivedData` by default
> - ⌘ `cache-derived-data-prefix` which is `__unspecified__` aka `" "` by default
> - ⌘ `cache-derived-data-suffix` which is `__unspecified__` aka `" "` by default

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

</br>

### ⌘ `with.platform`

_Target platform for the action_

**Type:**

- **`optional`**
- **`required`** for the following commands
  - `xcodebuild`
  - `xcodebuild-test`
  - `xcodebuild-raw`
  - `xcodebuild-test-raw`
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

### 🧩 Step examples:

#### Full:

```yaml
- name: Test CoolStuff
  uses: capturecontext/swift-package-action/build@3.0-beta.7
  with:
    xcode: 26.2
    workspace: Package.xcworkspace # custom workspace at the root of a repo
    cache-derived-data: true
    action: xcodebuild-test
    scheme: cool-stuff-package # likely to be a name of the package
    platform: iOS
    config: Debug
    beautify: true
    working-directory: '.'
```

#### Short:

```yaml
- name: Test CoolStuff
  uses: capturecontext/swift-package-action/build@3.0-beta.7
  with:
    workspace: Package.xcworkspace
    cache-derived-data: true
    action: xcodebuild-test
    scheme: cool-stuff-package
    platform: iOS
```

#### Just cache derived data

```yaml
- name: Cache derived data
  uses: capturecontext/swift-package-action/cache/derived-data@3.0-beta.7
```

### 📚 Workflow examples [outdated]

- [**`swift-existential-container`**](https://github.com/capturecontext/swift-existential-container/blob/main/.github/workflows/ci.yml)
- `swift-composable-architecture`
  - **_[Original](https://github.com/pointfreeco/swift-composable-architecture/blob/main/.github/workflows/ci.yml)_**
  - **_[SwiftPackageAction](https://github.com/capturecontext/swift-composable-architecture-ci-explorations/blob/main/.github/workflows/ci.yml)_**
