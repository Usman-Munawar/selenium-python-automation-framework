from selenium.webdriver.common.by import By

class ProductsPage:
    """
    Page Object for the Products Page.
    Contains actions and elements related to product listing.
    """

    # Locators
    TITLE = (By.CLASS_NAME, "title")
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        """Return page title text"""
        return self.driver.find_element(*self.TITLE).text

    def add_backpack_to_cart(self):
        """Add backpack product to cart"""
        self.driver.find_element(*self.BACKPACK_ADD_BUTTON).click()

    def get_cart_badge_count(self):
        """Return number of items in cart"""
        return self.driver.find_element(*self.CART_BADGE).text

    def open_cart(self):
        """Navigate to cart page"""
        self.driver.find_element(*self.CART_LINK).click()