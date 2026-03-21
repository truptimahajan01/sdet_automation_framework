from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        print(f"Entering email: {email}")
    
    def click_login(self):
        self.click("login_button_locator")


login = LoginPage("ChromeDriver")
login.enter_email("test@example.com")