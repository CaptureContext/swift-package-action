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

#### Nested actions:

- [**build**](./build/README.md)
- [**format**](./format/README.md)
- [**cache**](./cache/README.md)

> [!IMPORTANT]
>
> _Root action is able to run some actions, but the API wasn't updated and results are not tested, consider using nested actions. Documentation is deleted, currently we're deciding if we should keep such an umbrella action for public `v3` release or to remove it_

### 📚 Workflow examples

- [`capturecontext/cocoa-aliases`](https://github/capturecontext/cocoa-aliases)
- [`capturecontext/swift-equated`](https://github/capturecontext/swift-equated)
- [`capturecontext/swift-hashed`](https://github/capturecontext/swift-hashed)
- [`capturecontext/swift-marker-protocols`](https://github/capturecontext/swift-marker-protocols)
- [`capturecontext/swift-keypaths-extensions`](https://github/capturecontext/swift-keypaths-extensions)
- [`capturecontext/swift-interception`](https://github/capturecontext/swift-interception)
- [`capturecontext/combine-interception`](https://github/capturecontext/combine-interception)
- [`capturecontext/combine-cocoa`](https://github/capturecontext/combine-cocoa)
- [`capturecontext/swift-declarative-configuration`](https://github/capturecontext/swift-declarative-configuration)
- [`capturecontext/swift-associated-objects`](https://github/capturecontext/swift-associated-objects)
- [`capturecontext/swift-foundation-extensions`](https://github/capturecontext/swift-foundation-extensions)

#### Outdated:

- [`swift-existential-container`](https://github.com/capturecontext/swift-existential-container/blob/main/.github/workflows/ci.yml)
- `swift-composable-architecture`
  - **_[Original](https://github.com/pointfreeco/swift-composable-architecture/blob/main/.github/workflows/ci.yml)_**
  - **_[SwiftPackageAction](https://github.com/capturecontext/swift-composable-architecture-ci-explorations/blob/main/.github/workflows/ci.yml)_**


## License 🪪

This action is released under the MIT license. See [LICENSE](LICENSE) for details.

See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md) for inspiration references and their licences.
