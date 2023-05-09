#!/usr/bin/python3
"""
Python script to make an api call to
return the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"user-agent": "REDDITAPI/0.0.1"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data.get('data').get('subscribers')
        return subscribers
    else:
        return 0
