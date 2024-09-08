import requests
import json

URL = "http://127.0.0.1:8000/api/add-student/"
data = {
    'employee_name': 'Ashish Yadav',
    'employee_email':'ashishY@gmail.com',
    'employee_desgination':'React Developer',
    'employee_salary':18000,
}

json_data = json.dumps(data)

r = requests.post(url = URL, data=json_data)
data = r.json()
print(data)