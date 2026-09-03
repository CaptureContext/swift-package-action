from pathlib import Path
import subprocess

def swift_format(formatter_config=None):
  swift_files = [
    str(path)
    for path in Path(".").rglob("*.swift")
    if not any(part.startswith(".") for part in path.parts)
    and "Documentation.docc" not in path.parts
  ]

  if not swift_files:
    return

  command = [
    "swift", "format", "format",
    "--ignore-unparsable-files",
    "--in-place",
    "--parallel"
  ]

  if formatter_config not in [None, "__unspecified__"]:
    command.extend(["--configuration", formatter_config])

  subprocess.run(command + swift_files, check=True)
