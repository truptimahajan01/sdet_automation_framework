import pytest
import httpx
from api.models import User


@pytest.mark.api
@pytest.mark.asyncio
async def test_get_user_async():
    """Async GET /users/1 using httpx should return a valid User model."""
    async with httpx.AsyncClient(base_url="https://jsonplaceholder.typicode.com") as client:
        response = await client.get("/users/1")

    assert response.status_code == 200
    user = User(**response.json())
    assert user.id == 1


@pytest.mark.api
@pytest.mark.asyncio
async def test_get_all_posts_async():
    """Async GET /posts should return a non-empty list."""
    async with httpx.AsyncClient(base_url="https://jsonplaceholder.typicode.com") as client:
        response = await client.get("/posts")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0