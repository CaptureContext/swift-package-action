import os
import helpers.swift_format

if __name__ == "__main__":
  formatter = os.environ.get("FORMATTER", "swift-format")
  config = os.environ.get("CONFIG", None)

  if formatter == "swift-format":
    helpers.swift_format(
      formatter_config=config
    )

  else:
    print(f"Unsupported formatter: {formatter}")
