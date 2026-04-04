from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.config_reader import ConfigReader

def test_add_product_to_cart(driver):
    """
    Verify that user can add a product to cart
    and it appears in cart page.
    """
    config = ConfigReader.read_config()

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)

    # Login
    login_page.login(config["valid_username"], config["valid_password"])

    # Add product
    products_page.add_backpack_to_cart()

    # Open cart
    products_page.open_cart()

    # Verify product in cart
    items = cart_page.get_cart_items()
    assert "Sauce Labs Backpack" in items