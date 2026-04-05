from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    TITLE = (By.CLASS_NAME, "title")
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.find_element(*self.TITLE).text

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.BACKPACK_ADD_BUTTON).click()

    def get_cart_badge_count(self):
        return self.driver.find_element(*self.CART_BADGE).text

    def open_cart(self):
        cart = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        cart.click()