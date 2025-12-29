import os
import helpers

if __name__ == "__main__":
  scheme = os.environ("SCHEME", "Unspecified")
  helpers.generate_docs(scheme=scheme)
