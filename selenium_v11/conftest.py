import pytest
import yaml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("config.yaml") as f:
    data = yaml.safe_load(f)

browser_name = data["browser_name"]


@pytest.fixture()
def authorization():
    """Получение token"""
    res = requests.post(data["address"] + "gateway/login",
                        data={"username": data["username"], "password": data["password"]})
    return res.json()["token"]


@pytest.fixture()
def test_text1():
    """Заголовок чужого поста"""
    return "Тестовый заголовок"


@pytest.fixture()
def params_post():
    params = {"title": data["title_api"], "description": data["description_api"], "content": data["content_api"]}
    return params


@pytest.fixture(scope="session")
def browser():
    """Инициализация сайта"""

    if browser_name == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()   # закрытие элемента