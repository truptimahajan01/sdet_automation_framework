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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        print("\nText failed - cpturing screenshot")
    

def pytest_configure(config):
    print("\nStarting Test Execution...")