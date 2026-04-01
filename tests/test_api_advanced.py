from api.base_api import BaseAPIClient
from api.models import User

def test_get_user_valid():
    client = BaseAPIClient("https://jsonplaceholder.typicode.com")
    response = client.get("/users/1")
    assert response.status_code == 200

    data = response.json()
    user = User(**data)
    assert user.id == 1

def get_user_invalid():
    client = BaseAPIClient("https://jsonplaceholder.typicode.com")
    response = client.get("/users/999")
    assert response.status_code in [404, 200]

def test_create_user():
    client = BaseAPIClient("https://jsonplaceholder.typicode.com")
    payload = {
        "name": "Tarun",
        "job": "QA"
    }
    response = client.post("/posts", payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data

def test_create_invalid_user():
    client = BaseAPIClient("https://jsonplaceholder.typicode.com")
    payload = {}
    response = client.post("/posts", payload)
    assert response.status_code in [400, 201]

def test_multiple_users():
    client = BaseAPIClient("https://jsonplaceholder.typicode.com")
    response = client.get("/users")
    assert response.status_code == 200
    data = response.json()

    for user_data in data:
        user = User(**user_data)
        assert user.email is not None
