import yaml
import logging
from apimetods import get_posts_api, create_post_api, get_user_posts_api


with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(authorization, test_text1):
    """Проверка наличие чужого поста с определенным заголовком"""
    logging.info("Test 1 API Starting")
    res = get_posts_api(authorization)
    assert res is not None
    assert res.status_code == 200
    titles = [i["title"] for i in res.json()["data"]]
    assert test_text1 in titles, "test1 FAIL"


def test_step2(authorization, params_post):
    """Создание собственного поста"""
    logging.info("Test 2 API Starting")
    res = create_post_api(authorization, params_post)
    assert res is not None
    assert res.status_code == 200, "test2 FAIL"


def test_step3(authorization):
    """Проверка созданного поста по его описанию"""
    logging.info("Test 3 API Starting")
    res = get_user_posts_api(authorization)
    assert res is not None
    assert res.status_code == 200
    descriptions = [i["description"] for i in res.json()["data"]]
    assert data["description_api"] in descriptions
