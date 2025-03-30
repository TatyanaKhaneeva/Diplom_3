from pages.account_page import AccountPage


class TestAccount:


    # переход по клику на «Личный кабинет»
    def test_switch_to_account_by_click(self, driver, login):
        account_page = AccountPage(driver)
        account_page.check_account_page_open()

    # переход в раздел «История заказов»
    def test_switch_to_orders_history(self, driver, login):
        account_page = AccountPage(driver)
        account_page.check_switch_to_orders_history()

    # выход из аккаунта
    def test_log_out(self, driver, login):
        account_page = AccountPage(driver)
        account_page.log_out()
