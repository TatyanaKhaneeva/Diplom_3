import re
import allure
import time
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    # Клик по кнопке заказа и проверка всплывающего окна
    @allure.step("Кликаем по заказу и проверяем, что отображается всплывающее окно")
    def click_order_and_check_pop_up(self):
        self.wait_for_element(MainPageLocators.ORDERS_FEED_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDERS_FEED_BUTTON)
        self.find_element_and_click(OrderPageLocators.ORDER_LIST)
        self.check_element_is_visible(OrderPageLocators.STRUCTURE_TEXT)


    # Проверка наличия заказа из истории на страницу Лента заказов
    @allure.step('Проверяем, что заказ из истории заказов отображается на стр. Лента заказов')
    def check_order_from_history_is_on_orders_list(self):
        self.wait_for_element(MainPageLocators.SAUCES_BUTTON)
        self.scroll_to_element(MainPageLocators.SPICY_SAUCE)
        self.drag_and_drop(MainPageLocators.SPICY_SAUCE, MainPageLocators.CONSTRUCTOR_FIELD)
        self.scroll_to_element(MainPageLocators.BUN_INGREDIENT)
        self.drag_and_drop(MainPageLocators.BUN_INGREDIENT, MainPageLocators.CONSTRUCTOR_FIELD)
        self.find_element_and_click(MainPageLocators.ORDER_BUTTON)
        time.sleep(5)
        order_pop_up = self.find_element(MainPageLocators.ORDER_POP_UP)
        order_number = order_pop_up.text
        order_number_id = ''.join(filter(str.isdigit, order_number.split()[0]))
        self.find_element_and_click(MainPageLocators.CLOSE_POP_UP_ORDER)
        self.find_element_and_click(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_and_click(AccountPageLocators.HISTORY_BUTTON)
        self.wait_for_element(AccountPageLocators.FIRST_ORDER)
        self.scroll_to_element(AccountPageLocators.LAST_ORDER)
        order_in_account_pop_up = self.find_element(AccountPageLocators.LAST_ORDER)
        order_number_in_account = order_in_account_pop_up.text
        match = re.search(r'#(\d+)', order_number_in_account)
        if match:
            order_id = match.group(1).lstrip('0')
        assert order_number_id == order_id
        self.scroll_to_element(MainPageLocators.ORDERS_FEED_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDERS_FEED_BUTTON)
        order_locator = self.get_order_number_locator(order_id)
        self.check_element_is_visible(order_locator)


    # Проверка увеличения счетчика Выполнено за все время
    @allure.step('Проверяем, что счетчик Выполнено за все время увеличивается')
    def check_all_completed_orders_counter(self):
        self.wait_for_element(MainPageLocators.SAUCES_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDERS_FEED_BUTTON)
        self.wait_for_element(OrderPageLocators.ALL_ORDERS_COUNTER)
        all_completed_orders = self.find_element(OrderPageLocators.ALL_ORDERS_COUNTER)
        all_completed_orders_counter = all_completed_orders.text
        self.find_element_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.scroll_to_element(MainPageLocators.SPICY_SAUCE)
        self.drag_and_drop(MainPageLocators.SPICY_SAUCE, MainPageLocators.CONSTRUCTOR_FIELD)
        self.scroll_to_element(MainPageLocators.BUN_INGREDIENT)
        self.drag_and_drop(MainPageLocators.BUN_INGREDIENT, MainPageLocators.CONSTRUCTOR_FIELD)
        self.find_element_and_click(MainPageLocators.ORDER_BUTTON)
        time.sleep(5)
        self.wait_for_element(MainPageLocators.CLOSE_POP_UP_ORDER)
        self.find_element_and_click(MainPageLocators.CLOSE_POP_UP_ORDER)
        self.find_element_and_click(MainPageLocators.ORDERS_FEED_BUTTON)
        time.sleep(5)
        self.wait_for_element(OrderPageLocators.ALL_ORDERS_COUNTER)
        all_completed_orders_after_place_order = self.find_element(OrderPageLocators.ALL_ORDERS_COUNTER)
        all_completed_orders_after_place_order_counter = all_completed_orders_after_place_order.text
        assert all_completed_orders_counter < all_completed_orders_after_place_order_counter


    # проверка увеличения счетчика Выполнено за сегодня
    @allure.step('Проверяем, что счетчик Выполнено за сегодня увеличивается')
    def check_today_orders_counter(self):
        self.wait_for_element(MainPageLocators.SAUCES_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDERS_FEED_BUTTON)
        self.wait_for_element(OrderPageLocators.TODAY_ORDERS_COUNTER)
        today_orders = self.find_element(OrderPageLocators.TODAY_ORDERS_COUNTER)
        today_orders_counter = today_orders.text
        self.find_element_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.scroll_to_element(MainPageLocators.SPICY_SAUCE)
        self.drag_and_drop(MainPageLocators.SPICY_SAUCE, MainPageLocators.CONSTRUCTOR_FIELD)
        self.scroll_to_element(MainPageLocators.BUN_INGREDIENT)
        self.drag_and_drop(MainPageLocators.BUN_INGREDIENT, MainPageLocators.CONSTRUCTOR_FIELD)
        self.find_element_and_click(MainPageLocators.ORDER_BUTTON)
        time.sleep(5)
        self.wait_for_element(MainPageLocators.CLOSE_POP_UP_ORDER)
        self.find_element_and_click(MainPageLocators.CLOSE_POP_UP_ORDER)
        self.find_element_and_click(MainPageLocators.ORDERS_FEED_BUTTON)
        self.wait_for_element(OrderPageLocators.ALL_ORDERS_COUNTER)
        today_order_after_place_order = self.find_element(OrderPageLocators.TODAY_ORDERS_COUNTER)
        today_order_after_place_order_counter = today_order_after_place_order.text
        assert today_orders_counter < today_order_after_place_order_counter


    # Проверка появления заказа в поле В работе после создания заказа
    @allure.step('Проверяем, что заказ появляется в поле В работе')
    def check_in_progress_after_place_order(self):
        self.wait_for_element(MainPageLocators.SAUCES_BUTTON)
        self.scroll_to_element(MainPageLocators.SPICY_SAUCE)
        self.drag_and_drop(MainPageLocators.SPICY_SAUCE, MainPageLocators.CONSTRUCTOR_FIELD)
        self.scroll_to_element(MainPageLocators.BUN_INGREDIENT)
        self.drag_and_drop(MainPageLocators.BUN_INGREDIENT, MainPageLocators.CONSTRUCTOR_FIELD)
        self.find_element_and_click(MainPageLocators.ORDER_BUTTON)
        time.sleep(5)
        order_pop_up = self.find_element(MainPageLocators.ORDER_POP_UP)
        order_number = order_pop_up.text
        order_number_id = ''.join(filter(str.isdigit, order_number.split()[0]))
        self.find_element_and_click(MainPageLocators.CLOSE_POP_UP_ORDER)
        self.wait_for_element(MainPageLocators.ORDERS_FEED_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDERS_FEED_BUTTON)
        order_locator = self.get_order_in_progress_locator(order_number_id)
        self.check_element_is_visible(order_locator)
