import pytest
from jsonschema import validate
from api.models import User


# JSON Schema for validating user response structure
USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id":       {"type": "number"},
        "name":     {"type": "string"},
        "username": {"type": "string"},
        "email":    {"type": "string"}
    },
    "required": ["id", "name", "username", "email"]
}


@pytest.mark.api
@pytest.mark.smoke
def test_get_user_returns_200(api_client):
    """GET /users/1 should return HTTP 200."""
    response = api_client.get("/users/1")
    assert response.status_code == 200


@pytest.mark.api
def test_get_user_schema_is_valid(api_client):
    """GET /users/1 response should match the defined JSON schema."""
    response = api_client.get("/users/1")
    assert response.status_code == 200
    validate(instance=response.json(), schema=USER_SCHEMA)


@pytest.mark.api
def test_get_user_pydantic_model(api_client):
    """GET /users/1 response should be parseable into the User Pydantic model."""
    response = api_client.get("/users/1")
    assert response.status_code == 200
    user = User(**response.json())
    assert user.id == 1
    assert "@" in user.email


@pytest.mark.api
def test_create_post_returns_201(api_client):
    """POST /posts with valid payload should return HTTP 201 with an id."""
    payload = {"title": "Test Post", "body": "Hello World", "userId": 1}
    response = api_client.post("/posts", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()
