import yaml
import time
from testpage import OperationsHelper
import logging

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(browser):
    """Невозможность аутентификации с невалидными Username и Password"""

    logging.info("Test 1 UI Starting")     # подключаем логирование

    testpage = OperationsHelper(browser)    # инициализация страницы
    testpage.go_to_site()   # открываем страницу
    testpage.fill_login_field("test")    # ввод данных в поле логина
    testpage.fill_pass_field("test")     # ввод данных в поле пароля
    testpage.click_login_button()   # кликаем на кнопку Login
    time.sleep(data["wait"])

    assert testpage.get_error_text() == "401", "test1 FAIL"


def test_step2(browser):
    """Успешная аутентификация с валидными Username и Password"""

    logging.info("Test 2 UI Starting")

    testpage = OperationsHelper(browser)  # инициализация страницы
    testpage.fill_login_field(data["username"])  # ввод данных в поле логина
    testpage.fill_pass_field(data["password"])  # ввод данных в поле пароля
    testpage.click_login_button()  # кликаем на кнопку Login
    time.sleep(data["wait"])

    assert testpage.get_greeting_text() == "Hello, {}".format(data["username"]), "test2 FAIL"


def test_step3(browser):
    """Создание поста"""

    logging.info("Test 3 UI Starting")

    testpage = OperationsHelper(browser)  # инициализация страницы
    testpage.click_create_new_post_icon()   # клик по иконке Create new post
    time.sleep(data["wait"])
    testpage.fill_title_field(data["title_ui"])     # ввод данных в поле Title
    testpage.fill_description_field(data["description_ui"])  # ввод данных в поле Description
    testpage.fill_content_field(data["content_ui"])  # ввод данных в поле Content
    testpage.click_save_button()    # клик по кнопке SAVE
    time.sleep(data["wait"])

    assert testpage.get_post_title() == data["title_ui"], "test3 FAIL"


def test_step4(browser):
    """Проверка на наличие созданного поста на главной странице"""

    logging.info("Test 4 UI Starting")

    testpage = OperationsHelper(browser)  # инициализация страницы
    testpage.click_home_button()    # клик по кнопке Home
    time.sleep(data["wait"])

    assert testpage.get_title_of_first_post() == data["title_ui"], "test4 FAIL"


def test_step5(browser):
    """Проверка на наличие всплывающего окна при взаимодействии с Contact Us"""

    logging.info("Test 5 UI Starting")

    testpage = OperationsHelper(browser)  # инициализация страницы
    testpage.click_contact_button()  # клик по кнопке Contact
    testpage.fill_your_name_field(data["your_name"])    # ввод данных в поле Your name
    testpage.fill_your_email_field(data["your_email"])  # ввод данных в поле Your email
    testpage.fill_your_content_field(data["your_content"])  # ввод данных в поле Content
    testpage.click_contact_us_button()
    time.sleep(data["wait"])

    assert testpage.get_alert() == "Form successfully submitted", "test5 FAIL"
