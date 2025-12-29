import os

try:
    from .helpers import *
except ImportError:
    from helpers import *

if __name__ == "__main__":
  command = os.environ.get("COMMAND", "")
  platform = os.environ.get("PLATFORM", "")
  config = os.environ.get("CONFIG", "Debug")
  beautify = os.environ.get("BEAUTIFY", "quiet")
  scheme = os.environ.get("SCHEME", "Unspecified")
  workspace = os.environ.get("WORKSPACE", ".swiftpm/xcode/package.xcworkspace")
  
  derived_data_path = os.path.expanduser(f"~/.derivedData/{config}")
  destination = simulator.get_destination(platform)

  if command == "destination":
    print(destination)

  elif command == "warm-simulator":
    simulator.warm(
      destination=destination
    )

  elif command == "xcodebuild":
    xcode.build(
      test=False,
      destination=destination,
      config=config,
      scheme=scheme,
      workspace=workspace,
      derived_data_path=derived_data_path,
      beautify=beautify
    )

  elif command == "xcodebuild-test":
    xcode.build(
      test=True,
      destination=destination,
      config=config,
      scheme=scheme,
      workspace=workspace,
      derived_data_path=derived_data_path,
      beautify=beautify
    )

  elif command == "build-for-library-evolution":
    swift.build_for_library_evolution(
      scheme=scheme
    )

  elif command == "benchmark":
    swift.benchmark(
      scheme=scheme
    )

  else:
    print(f"Unknown command: {command}")
