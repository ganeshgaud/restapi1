import json
import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

# def get_resource(id=None):
#     d={}
#     if id is not None:
#         d={
#         'id':id,
#         }
#     resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(d))
#     print(resp.status_code)
#     print(resp.json())

def post_resource():
    d={
    'ename':'Arnav',
    'eaddr':'Karimnagar',
    'esal':5000,
    'eno':9999999999
    }
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(d))
    print(resp.status_code)
    print(resp.json())
post_resource()

#
# def put_resource(id=None):
#     d={
#     'id':id,
#     'esal':5000,
#     'ecell_no':1234567891
#     }
#     resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(d))
#     print(resp.status_code)
#     print(resp.json())
#
# def delete_resource(id=None):
#     d={
#     'id':id,
#     }
#     resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(d))
#     print(resp.status_code)
#     print(resp.json())
