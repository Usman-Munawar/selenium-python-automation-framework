from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config_reader import ConfigReader


def test_user_logout(driver):
    """
    Verify that user can logout successfully.
    """
    config = ConfigReader.read_config()

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    # Login
    login_page.login(config["valid_username"], config["valid_password"])

    # Logout
    products_page.logout()

    # Validate redirected to login page
    assert "saucedemo.com" in driver.current_url
    assert "inventory" not in driver.current_url