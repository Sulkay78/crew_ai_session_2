import yaml

# Load YAML file
with open(r"warmup/data.yaml", "r") as file:
    data = yaml.safe_load(file)   # safer than yaml.load

# Show the content
print("YAML content as Python dict:")
print(data) 

# If you want pretty formatting:
import pprint
pprint.pprint(data["database"]["content"])
 
 