import requests
import yaml
import logging

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def get_posts_api(authorization, owner="notMe"):
    header = {"X-Auth-Token": authorization}
    url = data["address"] + "api/posts"
    params = {"owner": "notMe"}

    try:
        res = requests.get(url, params=params, headers=header)
        logging.debug(
            f"Get request to {url} with params: {params} and headers: {header}. Response code: {res.status_code}")
        return res
    except:
        logging.exception(f"Exception occurred during get request to {url}")
        return None


def create_post_api(authorization, post_data):
    header = {"X-Auth-Token": authorization}
    url = data["address"] + "api/posts"

    try:
        res = requests.post(url, headers=header, data=post_data)
        logging.debug(
            f"Post request to {url} with headers: {header} and data: {post_data}. Response code: {res.status_code}")
        return res
    except:
        logging.exception(f"Exception occurred during post request to {url}")
        return None


def get_user_posts_api(authorization):
    header = {"X-Auth-Token": authorization}
    url = data["address"] + "api/posts"
    params = {"owner": "me"}

    try:
        res = requests.get(url, params=params, headers=header)
        logging.debug(
            f"Get request to {url} with params: {params} and headers: {header}. Response code: {res.status_code}")
        return res
    except:
        logging.exception(f"Exception occurred during get request to {url}")
        return None