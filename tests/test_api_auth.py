import pytest
from api.base_api import BaseAPIClient


@pytest.mark.api
def test_valid_auth(auth_headers):
    """Request with auth headers should return HTTP 200."""
    client = BaseAPIClient("https://jsonplaceholder.typicode.com")
    response = client.get("/users/1", headers=auth_headers)
    assert response.status_code == 200