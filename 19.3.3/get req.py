import requests

res = requests.get('https://petstore.swagger.io/v2/user/user1', headers={'accept': 'application/json',})

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

response_data = res.json() if 'application/json' in res.headers['Content-Type'] else res.text

print(res.status_code)
print(response_data)
