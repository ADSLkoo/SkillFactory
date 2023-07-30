import requests

res = requests.delete(f"https://petstore.swagger.io/v2/pet/9223372036854265719", headers={'accept': 'application/json'})

response_data = res.json() if 'application/json' in res.headers['Content-Type'] else res.text

print(res.status_code)
print(response_data)
