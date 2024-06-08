import json
import os
## Create Class for creating new dictionaries here


with open("characterinfo.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here

new_file = "characterinfo.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("characterinfo.json")
os.rename(new_file, "characterinfo.json")