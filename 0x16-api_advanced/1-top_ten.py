#!/usr/bin/python3

"""
python script to get top 10 titles from api
"""
import requests


def top_ten(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    headers = {'User-agent': 'MYAPI/0.0.1'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    try:
        my_data = data.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
