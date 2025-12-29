import subprocess

def build_for_library_evolution(scheme):
  subprocess.run(
    ["swift", "build"] + [
      "-q",
      "-c", "release",
      "--target", scheme,
      "-Xswiftc", "-emit-module-interface",
      "-Xswiftc", "-enable-library-evolution"
    ]
  )

def benchmark(scheme):
  subprocess.run(
    ["swift", "run"] + [
      "--configuration", "release", scheme
    ]
  )
