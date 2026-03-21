class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def enter_email(self, email):
        print(f"Entering email: {email}")

    def enter_password(self, password):
        print(f"Entering email: {password}")

if __name__ == "__main__":
    login = LoginPage("ChromeDriver")

    login.enter_email("test@exampl.py")
    login.enter_password("123456")
    

    
