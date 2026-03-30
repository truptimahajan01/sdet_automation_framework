from api.base_api import BaseAPIClient

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
