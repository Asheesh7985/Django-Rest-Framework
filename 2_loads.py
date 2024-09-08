import json

# Open and read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)
print(data)
python_data = json.dumps(data)
print(python_data)