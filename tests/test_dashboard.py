import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

BASE_URL = "https://www.saucedemo.com"


@pytest.mark.ui
def test_dashboard_loaded_after_login(browser):
    """Dashboard title should be visible after successful login."""
    browser.get(BASE_URL)
    LoginPage(browser).login("standard_user", "secret_sauce")
    dashboard = DashboardPage(browser)
    assert dashboard.is_dashboard_loaded() is True


@pytest.mark.ui
def test_dashboard_title_is_products(browser):
    """Dashboard heading should display 'Products'."""
    browser.get(BASE_URL)
    LoginPage(browser).login("standard_user", "secret_sauce")
    dashboard = DashboardPage(browser)
    assert dashboard.get_title() == "Products"


@pytest.mark.ui
def test_dashboard_product_count_is_nonzero(browser):
    """Product list should contain at least one item."""
    browser.get(BASE_URL)
    LoginPage(browser).login("standard_user", "secret_sauce")
    dashboard = DashboardPage(browser)
    assert dashboard.get_product_count() > 0
