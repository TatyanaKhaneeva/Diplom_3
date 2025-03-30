from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_LIST = (By.XPATH, "(//div[contains(@class, 'OrderHistory_dataBox__1mkxK')])[1]")  # первый элемент списка заказов
    STRUCTURE_TEXT = (By.XPATH, "//p[text()='Cостав']")  # текст Состав
    ALL_ORDERS_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[1]")  # общее кол-во заказов
    TODAY_ORDERS_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")  # выполнено за сегодня