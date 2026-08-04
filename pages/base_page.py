from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    """Base class for all Page Objects. Provides common Selenium interactions."""

    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    def click(self, locator: tuple):
        """Click an element identified by a (By, value) locator tuple."""
        logger.info(f"Clicking element: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator: tuple, text: str):
        """Clear a field and type text into it."""
        logger.info(f"Typing into element: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Return the visible text of an element."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_element_visible(self, locator: tuple, timeout: int = DEFAULT_TIMEOUT) -> bool:
        """Return True if element is visible within timeout, False otherwise."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_page_title(self) -> str:
        """Return the browser page title."""
        return self.driver.title