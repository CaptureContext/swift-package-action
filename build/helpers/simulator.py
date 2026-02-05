import subprocess
import json

def warm(destination):
  platform_id = destination.split("id=")[-1]
  
  if platform_id:
    if platform_id.startswith("macOS"):
      print("Couldn't warm simulator. Reason: macOS simulators are not supported.")
      return

    boot = ["xcrun", "simctl", "boot", platform_id]
    subprocess.run(boot, check=True)

    open = [
        "open", "-a", "Simulator", "--args",
        "-CurrentDeviceUDID", platform_id
    ]
    subprocess.run(open, check=True)

def get_destination(platform):
  if platform == "iOS":
    return f"iOS Simulator,id={udid_for('iOS', 'iPhone')}"
  elif platform == "macOS":
    return "macOS"
  elif platform == "macCatalyst":
    return "macOS,variant=Mac Catalyst"
  elif platform == "tvOS":
    return f"tvOS Simulator,id={udid_for('tvOS', 'TV')}"
  elif platform == "visionOS":  
    return f"visionOS Simulator,id={udid_for('visionOS', 'Vision')}"
  elif platform == "watchOS":
    return f"watchOS Simulator,id={udid_for('watchOS', 'Watch')}"
  else:
    return "__unsupported__"

def udid_for(platform, device):
  result = subprocess.run(
      ["xcrun", "simctl", "list", "--json", "devices", "available", device],
      capture_output=True,
      text=True
  )

  devices_json = json.loads(result.stdout)
  devices = devices_json.get("devices", {})
  
  platform_devices = []
  for runtime, runtime_devices in sorted(devices.items(), reverse=True):
    if platform in runtime:
      platform_devices.extend(runtime_devices)

  matching_devices = [
    d 
    for d in platform_devices 
      if device in d.get("name", "") 
      and d.get("isAvailable", True)
  ]

  matching_devices.sort(key=lambda d: d.get("name", ""), reverse=True)

  if matching_devices:
    return matching_devices[0].get("udid", "")
  return ""
