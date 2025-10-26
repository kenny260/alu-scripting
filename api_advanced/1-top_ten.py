#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Main function"""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return
    
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    
    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        
        # Check if the request was successful
        if RESPONSE.status_code != 200:
            print(None)
            return
            
        data = RESPONSE.json().get("data")
        
        # Check if data exists
        if data is None:
            print(None)
            return
            
        HOT_POSTS = data.get("children")
        
        # Check if children exists and is not empty
        if HOT_POSTS is None:
            print(None)
            return
            
        for post in HOT_POSTS:
            print(post.get('data').get('title'))
            
    except Exception:
        print(None)
