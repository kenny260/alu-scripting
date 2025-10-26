#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Main function"""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyRedditApp/0.0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code != 200:
            print(None)
            return

        json_data = response.json()
        
        if json_data.get("data") is None:
            print(None)
            return

        children = json_data.get("data").get("children")

        if children is None:
            print(None)
            return

        for post in children:
            title = post.get('data').get('title')
            print(title)

    except Exception:
        print(None)
