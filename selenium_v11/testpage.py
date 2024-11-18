from BassApp import BassPage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    """Класс с локаторами."""
    ids = dict()    # создаем пустой словарь
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)    # открываем и считываем файл с локаторами
    # используем 2 цикла, чтобы получить пары из файла
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BassPage):
    """
    Класс с методами
    """
    def enter_text_into_field(self, locator, word, description=None):
        """Вспомогательный метод обработки ошибок, а так же общая логика для методов ввода текста"""
        # description - чтобы в информационные сообщения попадали понятные названия локаторов
        # если description задан, то отображаем description
        # если нет, то отображаем locator
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send '{word}' to element {element_name}")
        field = self.find_element(locator)  # находим элемент
        if not field:   # если не нашли элемент
            logging.error(f"Element {locator} not found")
            return False
        # else не нужен, т.к. если не нашли элемент, то сразу выходим из функции
        try:
            field.clear()   # отчищаем поле
            field.send_keys(word)   # вписываем текст в поле
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True     # если ошибок не было вернем истину

    def click_button(self, locator, description=None):
        """Вспомогательный метод обработки ошибок, а так же общая логика для методов нажатия на кнопки"""
        # description - чтобы в информационные сообщения попадали понятные названия локаторов
        # если description задан, то отображаем description
        # если нет, то отображаем locator
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)  # находим элемент
        if not button:
            return False
        try:
            button.click()  # клик по кнопке
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        """Вспомогательный метод обработки ошибок, а так же общая логика для методов получения текста"""
        # description - чтобы в информационные сообщения попадали понятные названия локаторов
        # если description задан, то отображаем description
        # если нет, то отображаем locator
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)  # ищем элемент, но перед этим ждем
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text     # возвращаем только текст

# ENTER TEXT - методы ввода текста
    def fill_login_field(self, word):
        """Ввод данных в поле Username"""
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_INPUT_USERNAME"], word, description="login form")

    def fill_pass_field(self, word):
        """Ввод данных в поле Password"""
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_INPUT_PASSWORD"], word, description="password form")

    def fill_title_field(self, word):
        """Ввод данных в поле Title"""
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE"], word, description="title")

    def fill_description_field(self, word):
        """Ввод данных в поле Description"""
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION"], word, description="description")

    def fill_content_field(self, word):
        """Ввод данных в поле Content"""
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT"], word, description="content")

    def fill_your_name_field(self, word):
        """Ввод данных в поле Your name формы Contact us"""
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_INPUT_YOUR_NAME"], word, description="your name")

    def fill_your_email_field(self, word):
        """Ввод данных в поле Your email формы Contact us"""
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_INPUT_YOUR_EMAIL"], word, description="your email")

    def fill_your_content_field(self, word):
        """Ввод данных в поле Content формы Contact us"""
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_INPUT_CONTENT"], word, description="your contact content")

# GET TEXT - методы получения текста
    def get_error_text(self):
        """Метод получения и возврата текста сообщения об ошибке"""
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERR_LABEL"], description="error label")

    def get_greeting_text(self):
        """Метод получения и возврата текста приветствия при успешной аутентификации"""
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_GREETING_TEXT"], description="greeting text")

    def get_post_title(self):
        """Метод получения и возврата заголовка поста на странице поста"""
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_POST_TITLE"], description="post title")

    def get_title_of_first_post(self):
        """Метод получения и возврата заголовка первого поста на главной странице"""
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_FIRST_POST"], description="first post title")

    def get_alert(self):
        """Метод возврата текста alert"""
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text

# CLICK - клик по кнопке
    def click_login_button(self):
        """Клик по кнопке Login"""
        self.click_button(TestSearchLocators.ids["LOCATOR_BTN_LOGIN"], description="login")

    def click_create_new_post_icon(self):
        """Клик по иконке Create new post"""
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_BTN"], description="create new post")

    def click_save_button(self):
        """Клик по кнопке SAVE"""
        self.click_button(TestSearchLocators.ids["LOCATOR_BTN_SAVE"], description="save")

    def click_home_button(self):
        """Клик по кнопке Home"""
        self.click_button(TestSearchLocators.ids["LOCATOR_BTN_HOME"], description="home")

    def click_contact_button(self):
        """Клик по кнопке Contact"""
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="contact")

    def click_contact_us_button(self):
        """Клик по кнопке CONTACT US"""
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], description="contact us")
