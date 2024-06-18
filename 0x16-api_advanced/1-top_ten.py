#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    if not subreddit or type(subreddit) is not str:
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {}).get("children", [])
            if not data:
                print(None)
            else:
                for post in data:
                    print(post.get("data", {}).get("title", None))
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)
