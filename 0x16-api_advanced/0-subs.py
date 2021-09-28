#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the num of subscribers"""
    r = requests.get("https://reddit.com/r/{}/about.json".format(subreddit),
                     headers={"User-Agent": "custom"})
    if (r.status_code == 200):
        return r.json().get("data").get("subscribers")
    else:
        return 0
