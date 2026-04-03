import pytest
from utils.driver_factory import get_driver
from utils.config_reader import ConfigReader

@pytest.fixture
def driver():
    """
    Pytest fixture to initialize WebDriver before each test
    and close it after test execution.
    """
    driver = get_driver()

    # Load configuration
    config = ConfigReader.read_config()

    # Open base URL
    driver.get(config["base_url"])

    yield driver

    # Quit browser after test
    driver.quit()