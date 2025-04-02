from pages.account_page import AccountPage
from locators.account_page_locators import AccountPageLocators
from locators.forgot_password_page_locators import ForgotPasswordPageLocators



class TestAccount:


    # переход по клику на «Личный кабинет»
    def test_switch_to_account_by_click(self, driver, login):
        account_page = AccountPage(driver)
        account_page.check_account_page_open()
        assert account_page.check_element_is_visible(
            AccountPageLocators.PROFILE_BUTTON)
        assert account_page.check_element_is_visible(AccountPageLocators.HISTORY_BUTTON)



    # переход в раздел «История заказов»
    def test_switch_to_orders_history(self, driver, login):
        account_page = AccountPage(driver)
        account_page.check_switch_to_orders_history()
        assert account_page.check_element_is_visible(
            AccountPageLocators.ORDER_COMPLETED_TEXT)
        assert account_page.check_element_is_visible(AccountPageLocators.HISTORY_BUTTON_ACTIVE)


    # выход из аккаунта
    def test_log_out(self, driver, login):
        account_page = AccountPage(driver)
        account_page.log_out()
        assert account_page.check_element_is_not_visible(AccountPageLocators.PROFILE_BUTTON)

