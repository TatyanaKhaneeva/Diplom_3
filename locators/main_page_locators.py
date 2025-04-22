from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # кнопка Оформить заказ
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # кнопка Личный кабинет
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # кнопка Конструктор
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")  # кнопка Лента заказов
    LOG_IN_BUTTON = (By.XPATH, "//button[contains(., 'Войти в аккаунт')]")  # Вход на главной странице
    CREATE_BURGER_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']")  # текст Собери бургер
    READY_TEXT = (By.XPATH, "//p[text()='Готовы:']")  # текст Готовы
    BUN_INGREDIENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")  # кнопка Флюоресцентная булка
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")  # кнопка Counter (открывает поп-ап Детали ингридиента)
    CLOSE_POP_UP_INGREDIENT_DETAILS_BUTTON = (By.XPATH, "(//button[contains(@class, 'close_modified')])[1]")  # крестик на поп-апе Детали ингридианта
    SAUCES_BUTTON = (By.XPATH, "//h2[text()='Соусы']")  # кнопка Соусы
    SPICY_SAUCE = (By.XPATH, "//img[@alt='Соус Spicy-X']")  # Соус Spicy-X
    CONSTRUCTOR_FIELD = (By.XPATH, "//span[text()='Перетяните булочку сюда (верх)']")  # поле для создания бургера (верхняя булка)
    COUNTER = (By.XPATH, "(//p[contains(@class, 'counter_counter__num__3nue1')])[3]") # счетчик в правом верхнем углу над булкой
    ORDER_ID = (By.XPATH, "//p[text()='идентификатор заказа']")  # идентификатор заказа
    ORDER_POP_UP = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")  # поп-ап заказа
    CLOSE_POP_UP_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")