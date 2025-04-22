from pages.base_page import BasePage
from pages.forgot_password_page import ForgotPasswordPage
from constants import URLs
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from constants import Data


class TestResetPassword:

    # переход на страницу восстановления пароля по кнопке «Восстановить пароль»
    def test_switch_to_reset_password_by_click_on_reset_button(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(URLs.LOGIN_PAGE)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.click_reset_password_and_check_redirect()
        assert forgot_password_page.check_element_is_visible(ForgotPasswordPageLocators.RESETTING_PASSWORD_TEXT)

    # ввод почты и клик по кнопке «Восстановить»
    def test_reset_password_click(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(URLs.FORGOT_PASSWORD_PAGE)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.fill_in_email_and_reset(Data.REGISTRATION_EMAIL)
        assert forgot_password_page.check_element_is_visible(ForgotPasswordPageLocators.SAVE_BUTTON)


    # клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его
    def test_show_hide_password_button_activates_field(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(URLs.FORGOT_PASSWORD_PAGE)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.fill_in_email_and_reset(Data.REGISTRATION_EMAIL)
        forgot_password_page.fill_password_in("098765")
        forgot_password_page.check_visibility()
