import os
import subprocess
import re

def clean_docs_out(docs_out_path):
  if os.path.exists(f"{docs_out_path}/.git"):
    subprocess.run(["rm", "-rf", f"{docs_out_path}/.git"])
  if os.path.exists(f"{docs_out_path}/main"):
    subprocess.run(["rm", "-rf", f"{docs_out_path}/main"])

def get_tags():
  tags = subprocess.run(
    ["git", "tag", "-l", "--sort=-v:refname"],
    capture_output=True,
    text=True
  ).stdout.splitlines()
  return [tag for tag in tags if tag and re.search(r"\d+\.\d+\.0", tag)]

def remove_old_tags(tags):
  tags_to_remove = tags[6:]
  for tag in tags_to_remove:
    subprocess.run(["rm", "-rf", tag])

def generate_docs_for_tag(tag, scheme, docs_out_path, lowercase_scheme):
  if os.path.exists(f"{docs_out_path}/{tag}/data/documentation/{lowercase_scheme}"):
    print(f"✅ Documentation for {tag} already exists.")
  else:
    print(f"⏳ Generating documentation for {scheme} @ {tag} release.")
    
    subprocess.run(["rm", "-rf", f"{docs_out_path}/{tag}"])
    subprocess.run(["git", "checkout", "."])
    subprocess.run(["git", "checkout", tag])
    
    result = subprocess.run([
      "swift", "package",
      "--allow-writing-to-directory", f"{docs_out_path}/{tag}",
      "generate-documentation",
      "--target", scheme,
      "--output-path", f"{docs_out_path}/{tag}",
      "--transform-for-static-hosting",
      "--hosting-base-path", f"/swift-composable-architecture/{tag}"
    ])
    
    if result.returncode == 0:
      print(f"✅ Documentation generated for {scheme} @ {tag} release.")
    else:
      print(f"⚠️ Documentation skipped for {scheme} @ {tag}.")

def generate_docs(scheme):
  lowercase_scheme = scheme.lower()
  docs_out_path = "docs-out"

  clean_docs_out(docs_out_path)
  tags = get_tags()
  remove_old_tags(tags)

  tags_to_process = ["main"] + tags[:6]
  for tag in tags_to_process:
    generate_docs_for_tag(tag, scheme, docs_out_path, lowercase_scheme)
