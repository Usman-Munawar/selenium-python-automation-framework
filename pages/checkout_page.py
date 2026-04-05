from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FIRST_NAME_INPUT)
        )
        element.clear()
        element.send_keys(first_name)

    def enter_last_name(self, last_name):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LAST_NAME_INPUT)
        )
        element.clear()
        element.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.POSTAL_CODE_INPUT)
        )
        element.clear()
        element.send_keys(postal_code)

    def click_continue(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        button.click()

    def fill_checkout_information(self, first_name, last_name, postal_code):
        if first_name:
            self.enter_first_name(first_name)
        if last_name:
            self.enter_last_name(last_name)
        if postal_code:
            self.enter_postal_code(postal_code)
        self.click_continue()

    def get_error_message(self):
        error = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return error.text