import pytest

@pytest.fixture

def test_user():
    return {
        "email": "user@example.com",
        "password": "123456"
    }