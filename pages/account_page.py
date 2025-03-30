from pages.base_page import BasePage
import allure
from locators.account_page_locators import AccountPageLocators
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from locators.main_page_locators import MainPageLocators


class AccountPage(BasePage):

    # переход к личному кабинету
    @allure.step('Переходим в личный кабинет')
    def switch_to_account(self):
        self.find_element_and_click(MainPageLocators.ACCOUNT_BUTTON)
        self.check_element_is_visible(AccountPageLocators.PROFILE_BUTTON)


    # Проверка, что личный кабинет открыт
    @allure.step('Проверяем, что личный кабинет открыт')
    def check_account_page_open(self):
        self.find_element_and_click(MainPageLocators.ACCOUNT_BUTTON)
        self.check_element_is_visible(AccountPageLocators.PROFILE_BUTTON)
        self.check_element_is_visible(AccountPageLocators.HISTORY_BUTTON)

    # переход к истории заказов
    @allure.step('Переходим в историю заказов')
    def switch_to_orders(self):
        self.find_element_and_click(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_and_click(AccountPageLocators.HISTORY_BUTTON)
        self.check_element_is_visible(AccountPageLocators.ORDER_COMPLETED_TEXT)


    # Проверка, что совершен переход к Истории заказов
    @allure.step('Проверяем, что мы находимся на странице Истории заказов')
    def check_switch_to_orders_history(self):
        self.find_element_and_click(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_and_click(AccountPageLocators.HISTORY_BUTTON)
        self.wait_for_element(AccountPageLocators.HISTORY_BUTTON_ACTIVE)


    # выход
    @allure.step('Выход')
    def log_out(self):
        self.find_element_and_click(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_and_click(AccountPageLocators.EXIT_BUTTON)
        self.check_element_is_visible(ForgotPasswordPageLocators.EMAIL_FIELD)