#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, count=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    if count is None:
        count = {}

    word_list = [word.lower() for word in word_list]

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Python:100-count:v1.0"}
    params = {"limit": 100}

    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        children = data.get("children", [])

        for child in children:
            title = child["data"]["title"].lower().split()
            for word in word_list:
                count[word] = count.get(word, 0) + title.count(word)

        after = data.get("after")
        if after:
            return count_words(subreddit, word_list, after, count)
        else:
            sort_counts = sorted(count.items(), key=lambda kv: (-kv[1], kv[0]))

            for word, count in sort_counts:
                if count > 0:
                    print(f"{word}: {count}")

    except requests.exceptions.RequestException as e:
        print("Request failed: {}".format(e))
