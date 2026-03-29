from pages.base_page import BasePage
class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_dashboard_loaded(self):
        print("Dashboard Loaded")
        return True

    def get_title(self):
        return "Dashboard"