import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException



class BasePage:

    def __init__(self, driver):
        self.driver = driver


    # открытие страницы
    @allure.step('Открываем страницу')
    def open_page(self, page):
        self.driver.get(page)


    # ожидание элемента
    @allure.step('Ожидание элемента')
    def wait_for_element(self, locator):
        WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(locator)
        )


    # поиск элемента
    @allure.step('Находим элемент')
    def find_element(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)


    # скролл до элемента
    @allure.step('Скроллим до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    # поиск элемента и клик по нему
    @allure.step('Находим элемент и кликаем по нему')
    def find_element_and_click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)


    @allure.step('Проверяем, что элемент кликабельный через JavaScript')
    def check_element_is_clickable_js(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

        is_clickable = self.driver.execute_script("""
            var element = arguments[0];
            return element && 
                   element.offsetWidth > 0 && 
                   element.offsetHeight > 0 && 
                   window.getComputedStyle(element).pointerEvents !== 'none';
        """, element)

    # drag-and-drop элемента
    @allure.step('Drag-and-drop элемента')
    def drag_and_drop(self, source_locator, target_locator):
        source_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(source_locator))
        target_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(target_locator))

        # JavaScript для drag-and-drop'a
        self.driver.execute_script(
            "function createEvent(typeOfEvent) { " +
            "var event = document.createEvent('CustomEvent'); " +
            "event.initCustomEvent(typeOfEvent, true, true, null); " +
            "event.dataTransfer = { " +
            "data: {}, " +
            "setData: function(key, value) { this.data[key] = value; }, " +
            "getData: function(key) { return this.data[key]; } " +
            "}; " +
            "return event; " +
            "} " +
            "function dispatchEvent(element, typeOfEvent, event) { " +
            "if (element.dispatchEvent) { " +
            "element.dispatchEvent(event); " +
            "} else if (element.fireEvent) { " +
            "element.fireEvent('on' + typeOfEvent, event); " +
            "} " +
            "} " +
            "function simulateHTML5DragAndDrop(element, destination) { " +
            "var dragStartEvent = createEvent('dragstart'); " +
            "dispatchEvent(element, 'dragstart', dragStartEvent); " +
            "var dropEvent = createEvent('drop'); " +
            "dispatchEvent(destination, 'drop', dropEvent); " +
            "var dragEndEvent = createEvent('dragend'); " +
            "dispatchEvent(element, 'dragend', dragEndEvent); " +
            "} " +
            "simulateHTML5DragAndDrop(arguments[0], arguments[1]);",
            source_element,
            target_element
        )


    # формирование локатора для поиска заказа в ленте заказов
    @allure.step('Формируем локатор для поиска заказа')
    def get_order_number_locator(self, order_id):
        return (By.XPATH, f"//p[text()='#0{order_id}']")


    # формирование локатора для заказа в работе
    @allure.step('Формируем локатор для заказа в работе')
    def get_order_in_progress_locator(self, order_id):
        return (By.XPATH, f"//ul[contains(@class, 'OrderFeed_orderListReady')]/li[text()='{order_id}']")


    # добавление текста в форму
    @allure.title('Добавляем текст в форму')
    def add_text_to_form(self, locator, name):
        self.driver.find_element(*locator).send_keys(name)

    # проверка, что элемент виден на странице
    @allure.step('Проверяем видимость элемента')
    def check_element_is_visible(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except TimeoutException:
            return False

    @allure.step('Получаем текст элемента через JS')
    def get_element_text_js(self, locator):
        return self.driver.execute_script("return arguments[0].textContent;", self.driver.find_element(*locator))

    @allure.step('Ждем изменение ID')
    def wait_for_text_change(self, locator, initial_text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.get_element_text_js(locator) != initial_text
        )


    # проверка, что элемент не виден на странице
    @allure.step('Проверяем, что элемент не отображается')
    def check_element_is_not_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False





