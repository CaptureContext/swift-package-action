import subprocess

def build(
  test,
  destination,
  config, 
  scheme,
  workspace,
  derived_data_path,
  beautify
):
  flags = [
    "-configuration", config,
    "-derivedDataPath", derived_data_path,
    "-destination", f"platform={destination}",  # e.g. "platform=iOS Simulator,id=..."
    "-scheme", scheme,
    "-workspace", workspace,      # e.g. ".swiftpm/xcode/package.xcworkspace"
    "-skipMacroValidation",
  ]
  
  if test:
    run_xcodebuild_command(
      args=["test"] + flags,
      beautify=beautify
    )
  else:
    run_xcodebuild_command(
      args=flags,
      beautify=beautify
    )

def test_docs(scheme, destination):
  doc_warnings = subprocess.run(
    ["xcodebuild", "clean", "docbuild"] + [
      "-scheme", scheme,
      "-destination", f"platform={destination}",
      "-quiet"
    ],
    capture_output=True,
    text=True
  ).stdout

  if "couldn't be resolved to known documentation" in doc_warnings:
    print(f"xcodebuild docbuild failed:\n\n{doc_warnings}")
    exit(1)

def run_xcodebuild_command(args, beautify):
  xcodebuild_command = ["xcodebuild"] + args

  if beautify == "true":
    xcbeautify_command = ["xcbeautify"]
  elif beautify == "quiet":
    xcbeautify_command = ["xcbeautify", "--quiet"]
  else:
    xcbeautify_command = None

  if xcbeautify_command is None:
    subprocess.run(xcodebuild_command, check=True)
    return

  p1 = subprocess.Popen(
    xcodebuild_command,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
  )

  p2 = subprocess.Popen(
    xcbeautify_command,
    stdin=p1.stdout,
    text=True
  )

  p1.stdout.close()

  rc2 = p2.wait()
  rc1 = p1.wait()

  # "pipefail"
  if rc1 != 0:
    raise subprocess.CalledProcessError(rc1, xcodebuild_command)
  if rc2 != 0:
    raise subprocess.CalledProcessError(rc2, xcbeautify_command)
