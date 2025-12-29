import os

def swift_format(formatter_config=None):
  if formatter_config == None:
    flags = [
      "--ignore-unparsable-files",
      "--in-place"
    ]
  else:
    flags = [
      f"--configuration {formatter_config}",
      "--ignore-unparsable-files",
      "--in-place"
    ]

  format_command = ["swift", "format"] + flags

  command = [
    "find", ".",
    "-path", "*/Documentation.docc", "-prune", "-o",
    "-name", "*.swift",
    "-not", "-path", "*/.*", "-print0",
    "xargs", "-0", "|"
  ] + format_command

  os.subprocess.run(command)
