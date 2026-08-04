import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from api.base_api import BaseAPIClient
from config.config_loader import load_config


# ── UI Fixture ───────────────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def browser():
    """Provides a headless Chrome WebDriver for UI tests.

    Uses Selenium 4's built-in SeleniumManager for automatic driver management
    — no separate ChromeDriverManager call needed.
    """
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Selenium 4.6+ handles driver binary automatically via SeleniumManager
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# ── Config & API Fixtures ─────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def config():
    """Load the active environment config."""
    return load_config()


@pytest.fixture(scope="session")
def api_client(config):
    """Provides a configured BaseAPIClient using the active environment base_url."""
    return BaseAPIClient(config["base_url"])


# ── Data Fixtures ─────────────────────────────────────────────────────────────

@pytest.fixture
def test_user():
    return {
        "email": "user@example.com",
        "password": "Test@1234"
    }


@pytest.fixture
def auth_headers():
    return {
        "Authorization": "Bearer test_token_123",
        "Content-Type": "application/json"
    }


# ── Hooks ─────────────────────────────────────────────────────────────────────

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a screenshot on test failure and attach it to the Allure report."""
    import allure

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser")
        if driver and hasattr(driver, "save_screenshot"):
            screenshot_dir = Path("reports/screenshots")
            screenshot_dir.mkdir(parents=True, exist_ok=True)
            path = screenshot_dir / f"{item.name}.png"
            driver.save_screenshot(str(path))
            allure.attach.file(
                str(path),
                name="Screenshot on Failure",
                attachment_type=allure.attachment_type.PNG
            )


def pytest_configure(config):
    print("\n[START] Starting Test Execution...")