#!/usr/bin/python3
"""python script to return the top 10 posts from the reddit api"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"user-agent": "REDDITAPI/0.0.1"}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))

    else:
        print(None)
