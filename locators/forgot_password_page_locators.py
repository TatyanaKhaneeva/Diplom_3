from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    RESET_PASSWORD_BUTTON = (By.XPATH, "//a[contains(., 'Восстановить пароль')]")  # кнопка Восстановить пароль
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")  # кнопка Войти
    RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  # кнопка Восстановить
    RESETTING_PASSWORD_TEXT =(By.XPATH, "//h2[contains(., 'Восстановление пароля')]")  # Восстановление пароля текст на странице
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/../input")  # поле ввода email
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")  # кнопка Сохранить
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/../input")  # поле ввода пароля
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'password')]/div[contains(@class, 'input__icon')]") #кнопка Показать пароль
    PASSWORD_INPUT_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")  # проверка видимости поля на странице восстановления пароля