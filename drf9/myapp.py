import requests
import json

URL = "http://127.0.0.1:8000/api/"

# def get_data(id = None):
#     data = {}
#     if id is not None:
#         data = {'id':id}
#     json_data = json.dumps(data)
#     headers = {'content-Type':'application/json'}
#     r = requests.get(url=URL, headers=headers, data=json_data)
#     data = r.json()
#     print(data)

# get_data(2)

# def post_data():
    
#     data = {
#         'name':'Dileep',
#         'roll':104,
#         'city':'Kolkata'
#     }
#     json_data = json.dumps(data)
#     headers = {'content-Type':'application/json'}
#     r = requests.post(url=URL, headers=headers, data=json_data)
#     data = r.json()
#     print(data)

# post_data()

# def update_data():
    
#     data = {
#         'id':4,
#         'name':'Ram Singh Tomar',
#         'roll':110,
#         'city':'Puri'
#     }
#     json_data = json.dumps(data)
#     headers = {'content-Type':'application/json'}
#     r = requests.put(url=URL, headers=headers, data=json_data)
#     data = r.json()
#     print(data)

# update_data()

# def update_data():
    
#     data = {
#         'id':2,
#         'name':'Shiva Singh',
#         'roll':115,
#         'city':'Varansi'
#     }
#     json_data = json.dumps(data)
#     headers = {'content-Type':'application/json'}
#     r = requests.patch(url=URL, headers=headers, data=json_data)
#     data = r.json()
#     print(data)

# update_data()

def delete_data():
    
    data = {
        'id':2,
    }
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

delete_data()