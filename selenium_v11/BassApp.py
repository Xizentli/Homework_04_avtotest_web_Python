"""
Файл с базовыми классами страницы
"""
import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# базовый класс страницы
class BassPage:

    def __init__(self, driver):
        """Конструктор"""
        self.driver = driver
        self.base_url = "http://test-stand.gb.ru"

    def find_element(self, locator, time=10):
        """Поиск элемента"""
        # ищем элементы по locator и устанавливаем ожидание time для их появления
        # так же задаем сообщение message, которое выведется в случае, если элемент не найден
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")
        except:
            # если что-то пошло не так, то element может быть не назначен, поэтому присваиваем ему None (ничего)
            logging.exception("Find element exception")
            element = None
        return element

    def get_element_property(self, locator, property):
        """Получение свойств элемента"""
        element = self.find_element(locator)    # поиск элемента

        # если элемент найден и он не None/False/ или 0, то возвращаем элемент
        if element:
            return element.value_of_css_property(property)

        # если элемент не найден или он = None, то логируем ошибку и возвращаем None
        else:
            logging.error(f"Property {property} not found in element with locator {locator}")
            return None

    def go_to_site(self):
        """Метод открытия станицы сайта"""
        try:
            start_browsing = self.driver.get(self.base_url)  # возвращаем открытую страницу

        except:
            logging.exception("Exception while open site")
            start_browsing = None

        return start_browsing

    def get_alert_text(self):
        """Метод получения и возврата текста alert после успешной отправки формы"""
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception("Exception while alert")
            return None
