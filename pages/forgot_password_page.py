import allure
from constants import Data
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class ForgotPasswordPage(BasePage):

    # Переход на страницу восстановления пароля
    @allure.step('Переходим на страницу восстановления пароля со страницы Вход')
    def switch_to_reset_password(self):
        self.wait_for_element(MainPageLocators.LOG_IN_BUTTON)
        self.find_element_and_click(MainPageLocators.LOG_IN_BUTTON)
        self.wait_for_element(ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)
        self.find_element_and_click(ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)
        self.wait_for_element(ForgotPasswordPageLocators.RESETTING_PASSWORD_TEXT)


    # Проверка перехода на страницу Восстановление пароля при клике на кнопку Восстановить
    @allure.step('Переходим на станицу восстановления пароля по кнопке Восстановить')
    def click_reset_password_and_check_redirect(self):
        self.wait_for_element(ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)
        self.find_element_and_click(ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)
        self.wait_for_element(ForgotPasswordPageLocators.RESETTING_PASSWORD_TEXT)
        self.wait_for_element(ForgotPasswordPageLocators.EMAIL_FIELD)
        self.add_text_to_form(ForgotPasswordPageLocators.EMAIL_FIELD, Data.REGISTRATION_EMAIL)
        self.find_element_and_click(ForgotPasswordPageLocators.RESET_BUTTON)
        self.wait_for_element(ForgotPasswordPageLocators.RESETTING_PASSWORD_TEXT)


    # Ввод почты и нажатие кнопки Восстановить
    @allure.step('Вводим почту и нажимаем кнопку Восстановить')
    def fill_in_email_and_reset(self, email):
        self.wait_for_element(ForgotPasswordPageLocators.EMAIL_FIELD)
        self.add_text_to_form(ForgotPasswordPageLocators.EMAIL_FIELD, email)
        self.find_element_and_click(ForgotPasswordPageLocators.RESET_BUTTON)
        self.wait_for_element(ForgotPasswordPageLocators.SAVE_BUTTON)
        self.check_element_is_visible(ForgotPasswordPageLocators.SAVE_BUTTON)


    # Воод пароля и проверка работы кнопки Скрыть пароль/Показать пароль
    @allure.title('вводим пароль и проверяем кнопку Скрыть пароль')
    def fill_password_in_and_check_visibility(self, password):
        self.add_text_to_form(ForgotPasswordPageLocators.PASSWORD_FIELD, password)
        self.find_element_and_click(ForgotPasswordPageLocators.SHOW_PASSWORD_BUTTON)
        self.check_element_is_visible(ForgotPasswordPageLocators.PASSWORD_INPUT_ACTIVE)


    # Ввод пароля
    @allure.step('Вводим пароль')
    def fill_password_in(self, password):
        self.add_text_to_form(ForgotPasswordPageLocators.PASSWORD_FIELD, password)

    # Проверка работы кнопки Скрыть пароль/Показать пароль
    @allure.step('Проверяем кнопку Скрыть пароль/Показать пароль')
    def check_visibility(self):
        self.find_element_and_click(ForgotPasswordPageLocators.SHOW_PASSWORD_BUTTON)
        self.check_element_is_visible(ForgotPasswordPageLocators.PASSWORD_INPUT_ACTIVE)

