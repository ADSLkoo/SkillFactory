import requests
import json

class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'
        self.api_key = None  # Инициализируем переменную api_key значением None

    def get_api_key(self, email, password):

        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_new_pet(self, auth_key):
        data = {'name': 'name', 'animal_type': 'cat', 'age': '10'}
        headers = {'auth_key': auth_key['key'], 'accept': 'application/json'}
        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_new_pet_with_photo(self, auth_key):
        data = {'name': 'name', 'animal_type': 'cat', 'age': 10}
        headers = {'auth_key': auth_key['key'], 'accept': 'application/json'}
        files = {'pet_photo': ('pet_photo.jpg', open('2023-07-26_17-52-34.png', 'rb'), 'image/png')}
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data, files=files)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def get_list_of_pets(self, auth_key, filter):
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}
        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_set_photo(self, auth_key, pet_id):
        headers = {
            'auth_key': auth_key['key'],
            'accept': 'application/json',
        }

        files = {
            'pet_photo': ('pet_photo.jpg', open('2023-07-26_17-52-34.png', 'rb'), 'image/png')
        }

        url = f"{self.base_url}api/pets/set_photo/{pet_id}"
        res = requests.post(url, headers=headers, files=files)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def delete_pet(self, auth_key, pet_id):

        headers = {
            'auth_key': auth_key['key'],
            'accept': 'application/json',
        }

        files = {
            'pet_photo': ('pet_photo.jpg', open('2023-07-26_17-52-34.png', 'rb'), 'image/png')
        }

        url = f"{self.base_url}api/pets/set_photo/{pet_id}"
        res = requests.post(url, headers=headers, files=files)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def update_pet(self, auth_key, pet_id):
        data = {
            'name': 'newname',
            'animal_type': 'dog',
            'age': 99
        }

        headers = {
            'auth_key': auth_key['key'],
            'accept': 'application/json',
        }

        url = f"{self.base_url}api/pets/{pet_id}"
        res = requests.put(url, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text

        return status, result




