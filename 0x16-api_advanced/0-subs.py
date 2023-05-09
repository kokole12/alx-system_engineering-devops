#!/usr/bin/python3
"""
number of subscribers from redditapi
"""

import requests


def number_of_subscribers(subreddit):
    """
    python script to retrun number of suscribers from api
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    headers = {'User-agent': 'MYAPI/0.0.1'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    data = response.json()

    try:
        return data.get('data').get('subscribers')

    except Exception:
        return 0
