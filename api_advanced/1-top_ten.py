#!/usr/bin/python3
"""Script that fetches the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a valid subreddit.
    If the subreddit is invalid, prints None.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 10}

    response = requests.get(
        subreddit_url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data', {}).get('children', [])
    if not data:
        print(None)
        return

    for post in data:
        print(post.get('data', {}).get('title'))



