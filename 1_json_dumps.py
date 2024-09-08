import json
python_data = {'name':'Ashish Jaiswal','email':'ashish@gmail.com','salary':19000}
print(python_data)
print(type(python_data))

json_data = json.dumps(python_data)
print(json_data)
print(type(json_data))