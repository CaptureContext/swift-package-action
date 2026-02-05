<p align="center">
  <img src="../.media/swiftpm.png" alt="swift-package-action logo" height=300px/>
</p>

<h1 align="center">
  swift-package-action/format
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

### ⌘ `with.xcode`

_Xcode version_

**Type:** `optional`

**Default value:** `26.2`

> [!NOTE]
>
> _To skip `Select Xcode` step you can use set value to  `__unspecified__`_

</br>

### ⌘ `with.formatter`

_Formatter for the action_

**Type:** `optional`

**Default value:** `swift-format`

**Supported values:**

- `swift-format`

</br>

### ⌘ `with.config`

_Path to custom formatter configuration_

**Type:** `optional`

**Default value:** `__unspecified__`

</br>

### ⌘ `with.working-directory`

_Relative path to target directory_

**Type:** `optional`

**Default value:** `'.'`

</br>

### ⌘ `with.commit-message`

_Commit message for the action_

**Type:** `optional`

**Default value:** `[format]`

</br>

### ⌘ `with.branch`

_Branch for committing result of the action_

**Type:** `optional`

**Default value:** `main`

</br>

### 🧩 Step examples:

#### Full:


```yaml
- name: Test CoolStuff
  uses: capturecontext/swift-package-action/format@3.0-beta.11
  with:
    xcode: 26.2
    formatter: swift-format
    config: .custom-config
    branch: main
    commit-message: Run swift-format
    working-directory: '.'
```

#### Short:

```yaml
- name: Test CoolStuff
  uses: capturecontext/swift-package-action/format@3.0-beta.11
```
