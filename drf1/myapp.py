import json


def get_data(id=None):
    data={} 
    if id is not None:
        data = {'id':id}
    json_data = json.dumps