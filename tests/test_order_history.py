from pages.order_page import OrderPage


class TestOrderHistory:

    # если кликнуть на заказ, откроется всплывающее окно с деталями
    def test_details_pop_up(self, driver, login):
        order_page = OrderPage(driver)
        order_page.click_order_and_check_pop_up()

    # заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»
    def test_order_from_history_is_on_orders_page(self, driver, login):
        order_page = OrderPage(driver)
        order_page.check_order_from_history_is_on_orders_list()

    # при создании нового заказа счётчик Выполнено за всё время увеличивается
    def test_after_order_all_completed_orders_counter_grow(self, driver, login):
        order_page = OrderPage(driver)
        order_page.check_all_completed_orders_counter()

    # при создании нового заказа счётчик Выполнено за сегодня увеличивается
    def test_after_order_today_orders_counter_grow(self, driver, login):
        order_page = OrderPage(driver)
        order_page.check_today_orders_counter()

    # после оформления заказа его номер появляется в разделе В работе
    def test_after_placing_order_its_number_is_in_progress_list(self, driver, login):
        order_page = OrderPage(driver)
        order_page.check_in_progress_after_place_order()