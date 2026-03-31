from api.base_api import BaseAPIClient


def test_valid_auth(auth_headers):
    client = BaseAPIClient("https://jsonplaceholder.typicode.com")

    response = client.get("/users/1", headers=auth_headers)

    assert response.status_code == 200