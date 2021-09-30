#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """print the titles for given subreddit"""
    r = requests.get("https://www.reddit.com/r/%7B%7D.json?sort=hot&limit=10".
                     format(subreddit), headers={"User-Agent": "custom"})

    if (r.status_code == 200):
        for i in r.json().get("data").get("children"):
            print(i.get("data").get("title"))
    else:
        print("None")
