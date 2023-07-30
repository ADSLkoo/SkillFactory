import pytest
from api import PetFriends
from config import valid_email, valid_password

pf = PetFriends()

def test_get_api_key_for_valid_user():
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 200
    assert 'key' in result

@pytest.mark.xfail(raises=Exception)
def test_get_api_key_with_invalid_user_data():
    invalid_email = 'invalid_email@example.com'
    invalid_password = 'invalid_password'
    status, result = pf.get_api_key(invalid_email, invalid_password)
    assert status == 403


def test_post_new_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key)
    assert status == 200

@pytest.mark.xfail
def test_post_new_pet_with_invalid_auth_key():
    invalid_auth_key = {'key': 'invalid_auth_key'}
    status, result = pf.post_new_pet(auth_key=invalid_auth_key)
    assert status == 403


def test_post_new_pet_with_photo():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet_with_photo(auth_key)
    assert status == 200

@pytest.mark.xfail
def test_post_new_pet_with_photo_with_invalid_auth_key():
    invalid_auth_key = {'key': 'invalid_auth_key'}
    status, result = pf.post_new_pet_with_photo(auth_key=invalid_auth_key)
    assert status == 403


def test_get_all_pets_with_valid_key():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert 'pets' in result
    assert isinstance(result['pets'], list)
    assert len(result['pets']) > 0

@pytest.mark.xfail
def test_get_all_pets_with_invalid_key():
    invalid_auth_key = {'key': 'invalid_auth_key'}
    status, result = pf.get_list_of_pets(auth_key=invalid_auth_key, filter="my_pets")
    assert status == 403


def test_post_set_photo():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet_with_photo(auth_key)
    assert status == 200
    assert 'id' in result
    pet_id = result['id']
    status, result = pf.post_set_photo(auth_key, pet_id)
    assert status == 200

@pytest.mark.xfail
def test_post_set_photo_with_invalid_auth_key():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet_with_photo(auth_key)
    assert status == 200
    assert 'id' in result
    pet_id = result['id']
    status, result = pf.post_set_photo(auth_key, pet_id)
    assert status == 200
    invalid_auth_key = {'key': 'invalid_auth_key'}
    status, result = pf.post_set_photo(auth_key=invalid_auth_key, pet_id=pet_id)
    assert status == 403


def test_delete_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key)
    assert status == 200
    assert 'id' in result
    pet_id = result['id']
    status, result = pf.delete_pet(auth_key, pet_id)
    assert status == 200

@pytest.mark.xfail
def test_delete_pet_with_invalid_auth_key():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key)
    assert status == 200
    assert 'id' in result
    pet_id = result['id']
    invalid_auth_key = {'key': 'invalid_auth_key'}
    status, result = pf.delete_pet(auth_key=invalid_auth_key, pet_id=pet_id)
    assert status == 403


def test_update_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key)
    assert status == 200
    assert 'id' in result
    pet_id = result['id']
    status, result = pf.update_pet(auth_key, pet_id)
    assert status == 200

@pytest.mark.xfail
def test_update_pet_with_invalid_auth_key():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key)
    assert status == 200
    assert 'id' in result
    pet_id = result['id']
    invalid_auth_key = {'key': 'invalid_auth_key'}
    status, result = pf.update_pet(auth_key=invalid_auth_key, pet_id=pet_id)
    assert status == 403