from pages.base_page import BasePage
from constants import URLs
from pages.main_page import MainPage


class TestAccount:

    # переход по клику на «Конструктор»
    def test_switch_by_click_on_constructor(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(URLs.LOGIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_constructor_and_check_switch()

    # переход по клику на «Лента заказов»
    def test_switch_by_click_on_orders_feed(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(URLs.LOGIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_orders_and_check_switch()

    # если кликнуть на ингредиент, появится всплывающее окно с деталями
    def test_ingredient_details_pop_up(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(URLs.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_ingredient_and_check_pop_up()

    # всплывающее окно закрывается кликом по крестику
    def test_close_ingredient_details_pop_up(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(URLs.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_close_pop_up()

    # при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента
    def test_counter_after_adding_ingredient(self, driver, login):
        main_page = MainPage(driver)
        main_page.add_ingredient_and_check_counter()

    # залогиненный пользователь может оформить заказ
    def test_place_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.place_order_and_check()