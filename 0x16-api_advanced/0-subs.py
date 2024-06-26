#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API for a given subreddit
    Return: 0 if invalid subreddit is given
    """
    if not subreddit or type(subreddit) is not str:
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Python:0-subs:v1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0
