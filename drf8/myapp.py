import requests
import json

URL = "http://127.0.0.1:8000/api/"

# def get_data(id=None):
#     data = {}
#     if id is not None:
#         data = {'id':id}
#     json_data = json.dumps(data)
#     headers = {'content-Type':'application/json'}
#     r = requests.get(url=URL,headers=headers, data=json_data)
#     data = r.json()
#     print(data)

# get_data()

# def post_data():
#     data = {
#         'name':'dileep',
#         'city':'Mau'
#     }
#     json_data = json.dumps(data)
#     headers = {'content-Type':'application/json'}
#     r = requests.post(url=URL ,headers=headers, data = json_data)
#     data = r.json()
#     print(data)
# post_data()


# def update_data():

#     data = {
#         'id':4,
#         'name':'vikash',
#         'city':'Kanpur Dehat'
#     }
#     json_data = json.dumps(data)
#     headers = {'content-Type':'application/json'}
#     r = requests.put(url=URL ,headers=headers, data = json_data)
#     data = r.json()
#     print(data)
# update_data()


def delete_data():
    data={'id':4}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.delete(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)
delete_data()