import requests

res = requests.post('https://petstore.swagger.io/v2/pet', headers={'accept': 'application/json','Content-Type': 'application/json'})

data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "awww"
  },
  "name": "awww",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "awww"
    }
  ],
  "status": "available"
}

response_data = res.json() if 'application/json' in res.headers['Content-Type'] else res.text

print(res.status_code)
print(response_data)
