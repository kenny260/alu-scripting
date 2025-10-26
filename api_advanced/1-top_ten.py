#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Main function"""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data")

        # Check if data exists
        if data is None:
            print(None)
            return

        hot_posts = data.get("children")

        # Check if children exists
        if hot_posts is None or len(hot_posts) == 0:
            print(None)
            return

        for post in hot_posts:
            title = post.get('data').get('title')
            if title:
                print(title)

    except Exception:
        print(None)
