import os
from . helpers.echo import *

if __name__ == "__main__":
  text = os.environ.get("TEXT", "No echo")
  echo(text)
