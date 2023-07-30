import requests

res = requests.put('https://petstore.swagger.io/v2/user/user1', headers={'accept': 'application/json','Content-Type': 'application/json'})

data = {
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
}

if 'application/json' in res.headers['Content-Type']:
    response_data = res.json()
else:
    response_data = res.text

print(res.status_code)
print(response_data)