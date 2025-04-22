import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):


    # Конструктор
    @allure.step('Нажимаем на кнопку Конструктор и проверяем переход на данную страницу')
    def click_constructor_and_check_switch(self):
        self.wait_for_element(MainPageLocators.ORDERS_FEED_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDERS_FEED_BUTTON)
        self.check_element_is_visible(MainPageLocators.READY_TEXT)
        self.wait_for_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.find_element_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.check_element_is_visible(MainPageLocators.CREATE_BURGER_TEXT)

    # Лента заказов
    @allure.step('Нажимаем на кнопку Лента заказов и проверяем переход на данную страницу')
    def click_orders_and_check_switch(self):
        self.wait_for_element(MainPageLocators.ORDERS_FEED_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDERS_FEED_BUTTON)
        self.check_element_is_visible(MainPageLocators.READY_TEXT)


    # Проверка всплывающего окна
    @allure.step('Нажимаем на ингредиент и проверяем pop-up')
    def click_ingredient_and_check_pop_up(self):
        self.wait_for_element(MainPageLocators.BUN_INGREDIENT)
        self.find_element_and_click(MainPageLocators.BUN_INGREDIENT)
        self.check_element_is_visible(MainPageLocators.INGREDIENT_DETAILS)


    # Закрытие всплывающего окна
    @allure.step('Нажимаем на крестик на pop-up и проверяем, что оно закрылось')
    def click_close_pop_up(self):
        self.wait_for_element(MainPageLocators.BUN_INGREDIENT)
        self.find_element_and_click(MainPageLocators.BUN_INGREDIENT)
        self.check_element_is_visible(MainPageLocators.INGREDIENT_DETAILS)
        self.wait_for_element(MainPageLocators.CLOSE_POP_UP_INGREDIENT_DETAILS_BUTTON)
        self.find_element_and_click(MainPageLocators.CLOSE_POP_UP_INGREDIENT_DETAILS_BUTTON)
        self.check_element_is_not_visible(MainPageLocators.INGREDIENT_DETAILS)


    # Добавление ингредиента
    @allure.step('Добавляем ингредиент и проверяем счетчик')
    def add_ingredient_and_check_counter(self):
        self.wait_for_element(MainPageLocators.SAUCES_BUTTON)
        self.find_element_and_click(MainPageLocators.SAUCES_BUTTON)
        self.drag_and_drop(MainPageLocators.SPICY_SAUCE, MainPageLocators.CONSTRUCTOR_FIELD)
        counter_element = self.find_element(MainPageLocators.COUNTER)
        assert counter_element.text == "1"


    # Оформление заказа
    @allure.step('Оформляем заказ')
    def place_order_and_check(self):
        self.wait_for_element(MainPageLocators.ORDER_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDER_BUTTON)
        self.check_element_is_visible(MainPageLocators.ORDER_POP_UP)
        self.check_element_is_visible(MainPageLocators.ORDER_ID)


    # Закрытие всплываюещго окна заказа
    @allure.step('Закрываем pop-up заказа')
    def click_close_order_pop_up(self):
        self.wait_for_element(MainPageLocators.ORDER_POP_UP)
        self.find_element_and_click(MainPageLocators.CLOSE_POP_UP_ORDER)
        self.check_element_is_not_visible(MainPageLocators.ORDER_POP_UP)