from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from utils.config_reader import ConfigReader

def test_successful_checkout(driver):
    config = ConfigReader.read_config()

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)

    
    login_page.login(config["valid_username"], config["valid_password"])
    products_page.add_backpack_to_cart()
    products_page.open_cart()
    cart_page.click_checkout()
    checkout_page.fill_checkout_information("Usman", "Munawar", "12345")
    checkout_overview_page.click_finish()


    assert checkout_complete_page.get_success_message() == "Thank you for your order!"