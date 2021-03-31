import time
import requests
from pprint import pprint


def questions_from_stackoverflow():
    titles_dict = {}
    now = int(time.time())
    url = "https://api.stackexchange.com/2.2/questions"
    params = {"site": "stackoverflow", "fromdate": now - 172800, "todate": now, "tagged": "Python"}
    response = requests.get(url, params=params, timeout=5)
    for item in response.json()["items"]:
        titles_dict[item["title"]] = item["link"]
    return titles_dict


pprint(questions_from_stackoverflow(), width=150)
