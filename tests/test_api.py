from api.base_api import BaseAPIClient
from jsonschema import validate

def test_get_user():
    client = BaseAPIClient("https://jsonplaceholder.typicode.com")
    response = client.get("/users/1")
    assert response.status_code == 200

def test_create_users():
    client = BaseAPIClient("https://jsonplaceholder.typicode.com")
    data = {
        "name": "Tarun",
        "job": "qa"
    }
    response = client.post("/posts", data)
    assert response.status_code == 201

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"}
    },
    "required": ["id", "name", "email"]
}

def test_get_user():
    client = BaseAPIClient("https://jsonplaceholder.typicode.com")
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    validate(instance=data, schema=user_schema)

def test_create_users():
    client = BaseAPIClient("https://jsonplaceholder.typicode.com")
    data = {
        "name": "Tarun",
        "job": "qa"
    }
    response = client.post("/posts", data)
    assert response.status_code == 201
    response_data = response.json()
    assert "id" in response_data
