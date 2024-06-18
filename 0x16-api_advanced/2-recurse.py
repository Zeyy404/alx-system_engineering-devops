#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list of the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, return None.
    """
    if not subreddit or type(subreddit) is not str:
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Python:2-recurse:v1.0"}
    params = {"limit": 100}

    if after:
        params['after'] = after

        try:
            response = requests.get(url, headers=headers, params=params, allow_redirects=False)
            response.raise_for_status()

            data = response.json()
            children = data['data']['children']

            if not children:
                return hot_list

            for post in children:
                hot_list.append(post['data']['title'])

            after = data['data']['after']
            return recurse(subreddit, hot_list, after)

        except requests.exceptions.RequestException:
            return None
