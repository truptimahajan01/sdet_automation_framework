import pytest
from api.models import User


@pytest.mark.api
def test_get_user_valid(api_client):
    """Valid user ID should return correct user data validated by Pydantic model."""
    response = api_client.get("/users/1")
    assert response.status_code == 200
    user = User(**response.json())
    assert user.id == 1
    assert "@" in user.email


@pytest.mark.api
def test_get_nonexistent_user_returns_404(api_client):
    """Nonexistent user ID should return HTTP 404."""
    response = api_client.get("/users/9999")
    assert response.status_code == 404


@pytest.mark.api
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_multiple_users(api_client, user_id):
    """Parametrized test: verify multiple user IDs return valid Pydantic models."""
    response = api_client.get(f"/users/{user_id}")
    assert response.status_code == 200
    user = User(**response.json())
    assert user.id == user_id
    assert user.email is not None


@pytest.mark.api
def test_create_user_post(api_client):
    """POST with valid payload should return 201 with an id in the response."""
    payload = {"title": "New Post", "body": "Content", "userId": 1}
    response = api_client.post("/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data


@pytest.mark.api
def test_get_all_users_returns_list(api_client):
    """GET /users should return a non-empty list."""
    response = api_client.get("/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
