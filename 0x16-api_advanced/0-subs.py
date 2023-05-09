#!/usr/bin/python3
"""
Python script to make an api call to
return the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"user-agent": "REDDITAPI/0.0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()
    subscribers = data.get('data').get('subscribers')
    try:
        return subscribers
    except Exception:
        return 0
