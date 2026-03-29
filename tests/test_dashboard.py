from pages.dashboard_page import DashboardPage

def test_dashboard_loaded(browser):
    dashboard = DashboardPage(browser)
    assert dashboard.is_dashboard_loaded() is True

def test_dashboard_title(browser):
    dashboard = DashboardPage(browser)
    assert dashboard.get_title() == "Dashboard"

def test_dashboard_not_none(browser):
    dashboard = DashboardPage(browser)
    assert dashboard.get_title() is not None

