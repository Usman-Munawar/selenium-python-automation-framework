from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config_reader import ConfigReader

def test_valid_login(driver):
    """
    Verify that user can login with valid credentials
    and is redirected to Products page.
    """
    config = ConfigReader.read_config()

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    # Perform login
    login_page.login(config["valid_username"], config["valid_password"])

    # Validate successful login
    assert products_page.get_page_title() == "Products"


def test_invalid_login(driver):
    """
    Verify that error message appears with invalid credentials.
    """
    config = ConfigReader.read_config()

    login_page = LoginPage(driver)

    # Perform login with invalid credentials
    login_page.login(config["invalid_username"], config["invalid_password"])

    # Validate error message
    assert "Username and password do not match" in login_page.get_error_message()