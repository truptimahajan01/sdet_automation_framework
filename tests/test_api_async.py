import pytest
import httpx
from api.models import User
from api.base_api import BaseAPIClient


@pytest.mark.asyncio
async def test_get_user_async():
    async with httpx.AsyncClient(base_url="https://jsonplaceholder.typicode.com") as client:
        response = await client.get("/users/1")

    assert response.status_code == 200

    user = User(**response.json())

    assert user.id == 1


def test_get_posts():
    client = BaseAPIClient("https://jsonplaceholder.typicode.com")

    response = client.get("/posts/1")

    assert response.status_code == 200