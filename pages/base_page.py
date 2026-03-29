from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        print(f"Clicking on element {locator}")

    def wait_for_element(self, locator, timeout=10):
        print(f"Waiting for element: {locator}")
        return True

    def click(self, locator):
        self.wait_for_element(locator)
        print(f"Clicking {locator}")

    def type_text(self, locator, text):
        self.wait_for_element(locator)
        print(f"Typing {text} into {locator}")
    
    def test_dashbord_title_not_empty(browser):
        dashboard = dashboard(browser)
        assert dashboard.get_title() != ""

    def test_dashboard_loaded_again(browser):
        dashboard = dashboard(browser)
        assert dashboard.is_dashboard_loaded()