from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    """Page Object for the Inventory/Dashboard page (SauceDemo)."""

    # Locators
    PAGE_TITLE   = (By.CLASS_NAME, "title")
    PRODUCT_LIST = (By.CLASS_NAME, "inventory_item")

    def get_title(self) -> str:
        """Return the page heading text."""
        return self.get_text(self.PAGE_TITLE)

    def is_dashboard_loaded(self) -> bool:
        """Return True if the dashboard title is visible."""
        return self.is_element_visible(self.PAGE_TITLE)

    def get_product_count(self) -> int:
        """Return the number of product items displayed."""
        products = self.driver.find_elements(*self.PRODUCT_LIST)
        return len(products)