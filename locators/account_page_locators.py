from selenium.webdriver.common.by import By


class AccountPageLocators:
    INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/../input")  # ввод email
    INPUT_PASSWORD = (By.XPATH, "//label[text()='Пароль']/../input")  # ввод пароля
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")  # кнопка Войти
    PROFILE_BUTTON = (By.XPATH, "//a[text()='Профиль']")  # кнопка Профиль
    HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")  # кнопка История заказов
    HISTORY_BUTTON_ACTIVE = (By.XPATH, "//a[contains(@class, 'Account_link__2ETsJ') and @href='/account/order-history']")
    FIRST_ORDER = (By.XPATH, "(//div[contains(@class, 'OrderHistory_textBox')])[1]")  # первый заказ
    LAST_ORDER = (By.XPATH, "(//div[contains(@class, 'OrderHistory_textBox')])[last()]")  # последний заказ
    ORDER_COMPLETED_TEXT = (By.XPATH, "//p[text()='Выполнен']")  # текст заказа Выполнен
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # выход
