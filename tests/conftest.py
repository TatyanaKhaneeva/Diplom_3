import pytest
from factory import WebDriverFactory
from pages.login_page import LoginPage

BROWSERS = ["chrome", "firefox"]

@pytest.fixture(params=BROWSERS)
def driver(request):
    browser_name = request.param
    driver = WebDriverFactory.get_driver(browser_name)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()
    yield
