from selenium.webdriver.common.by import By

class LoginPage:
    """
    Page Object for the Login Page.
    Contains locators and actions related to login functionality.
    """

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        """Enter username into input field"""
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        """Enter password into input field"""
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        """Click on login button"""
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        """Perform complete login action"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """Return error message text if login fails"""
        return self.driver.find_element(*self.ERROR_MESSAGE).text