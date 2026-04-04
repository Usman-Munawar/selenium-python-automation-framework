from selenium.webdriver.common.by import By

class CartPage:
    """
    Page Object for Cart Page.
    Handles cart-related actions and validations.
    """

    # Locators
    CART_ITEMS = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        """Return list of item names in cart"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        return [item.text for item in items]

    def click_checkout(self):
        """Click checkout button"""
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()