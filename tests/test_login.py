import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

BASE_URL = "https://www.saucedemo.com"


@pytest.mark.ui
@pytest.mark.smoke
def test_valid_login_redirects_to_inventory(browser):
    """Valid credentials should redirect to the inventory page."""
    browser.get(BASE_URL)
    login = LoginPage(browser)
    login.login("standard_user", "secret_sauce")
    assert "inventory" in browser.current_url


@pytest.mark.ui
def test_invalid_login_shows_error_message(browser):
    """Invalid credentials should display a visible error message."""
    browser.get(BASE_URL)
    login = LoginPage(browser)
    login.login("invalid_user", "wrong_password")
    error = login.get_error_message()
    assert "Username and password do not match" in error


@pytest.mark.ui
def test_dashboard_displays_products_after_login(browser):
    """After successful login, the inventory page should display products."""
    browser.get(BASE_URL)
    login = LoginPage(browser)
    login.login("standard_user", "secret_sauce")
    dashboard = DashboardPage(browser)
    assert dashboard.is_dashboard_loaded()
    assert dashboard.get_product_count() > 0
