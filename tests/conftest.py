import pytest

@pytest.fixture

def test_user():
    return {
        "email": "user@example.com",
        "password": "123456"
    }

@pytest.fixture(scope="session")
def browser():
    driver = "ChromeDriver"   # dummy value
    yield driver
