#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Main function"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "python:myapp:v1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json().get("data")
            children = data.get("children")
            
            for post in children:
                print(post.get('data').get('title'))
        else:
            print(None)
            
    except Exception:
        print(None)
