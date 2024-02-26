import pytest
import requests
import random
import string

from constants import Constants, Endpoints


@pytest.fixture
def create_payload_and_then_delete_user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    email = generate_random_string(5) + "@yandex.ru"
    password = generate_random_string(10)
    name = generate_random_string(10)
    payload = {"email": email, "password": password, "name": name}
    yield payload
    token = ""
    response_del = requests.delete(f"{Constants.URL}{Endpoints.DELETE_USER}",
                                   headers={'Authorization': token})


@pytest.fixture
def create_user_for_login_and_then_delete_user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    email = generate_random_string(5) + "@yandex.ru"
    password = generate_random_string(10)
    name = generate_random_string(10)
    payload = {"email": email, "password": password, "name": name}
    resp_create = requests.post(f"{Constants.URL}{Endpoints.CREATE_USER}",
                                data=payload)
    token_with_bearer = resp_create.json()["accessToken"]
    user_token = token_with_bearer.split()
    token = user_token[1]
    payload_login = {"email": email, "password": password}
    fix = [payload_login, token]
    yield fix
    response_del = requests.delete(f"{Constants.URL}{Endpoints.DELETE_USER}",
                                   headers={'Authorization': token})


@pytest.fixture
def create_user_then_delete_user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    email = generate_random_string(5) + "@yandex.ru"
    password = generate_random_string(10)
    name = generate_random_string(10)
    payload = {"email": email, "password": password, "name": name}
    resp_create = requests.post(f"{Constants.URL}{Endpoints.CREATE_USER}",
                                data=payload)
    token_with_bearer = resp_create.json()["accessToken"]
    user_token = token_with_bearer.split()
    token = user_token[1]
    fix = [payload, token]
    yield fix
    response_del = requests.delete(f"{Constants.URL}{Endpoints.DELETE_USER}",
                                   headers={'Authorization': token})


@pytest.fixture
def create_user_unauthorized_then_delete_user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    email = generate_random_string(5) + "@yandex.ru"
    password = generate_random_string(10)
    name = generate_random_string(10)
    payload = {"email": email, "password": password, "name": name}
    resp_create = requests.post(f"{Constants.URL}{Endpoints.CREATE_USER}",
                                data=payload)
    token_with_bearer = resp_create.json()["accessToken"]
    user_token = token_with_bearer.split()
    token = user_token[1]
    yield resp_create
    response_del = requests.delete(f"{Constants.URL}{Endpoints.DELETE_USER}",
                                   headers={'Authorization': token})


@pytest.fixture
def create_user_and_order_then_delete_user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    email = generate_random_string(5) + "@yandex.ru"
    password = generate_random_string(10)
    name = generate_random_string(10)
    payload = {"email": email, "password": password, "name": name}
    resp_create = requests.post(f"{Constants.URL}{Endpoints.CREATE_USER}",
                                data=payload)
    token_with_bearer = resp_create.json()["accessToken"]
    user_token = token_with_bearer.split()
    token = user_token[1]
    payload_order = {"ingredients": ["61c0c5a71d1f82001bdaaa6d",
                                     "61c0c5a71d1f82001bdaaa70",
                                     "61c0c5a71d1f82001bdaaa72"]}
    resp_order = requests.post(f"{Constants.URL}{Endpoints.CREATE_ORDER}",
                               headers={"Authorization": token},
                               data=payload_order)
    number_order = resp_order.json()["order"]["number"]
    fix = [number_order, token]
    yield fix
    response_del = requests.delete(f"{Constants.URL}{Endpoints.DELETE_USER}",
                                   headers={'Authorization': token})
