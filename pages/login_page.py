from constants import URLs, Data
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def open(self):
        self.driver.get(URLs.LOGIN_PAGE)


    def login(self):
        self.wait_for_element(AccountPageLocators.INPUT_PASSWORD)
        self.add_text_to_form(AccountPageLocators.INPUT_EMAIL, Data.LOGIN)
        self.add_text_to_form(AccountPageLocators.INPUT_PASSWORD, Data.PASSWORD)
        self.find_element_and_click(AccountPageLocators.BUTTON_ENTER)
        self.check_element_is_visible(MainPageLocators.ORDER_BUTTON)


