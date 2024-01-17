#!/usr/bin/python3
"""
module: 1-top_ten
Holds a function - top_ten(subreddit)
"""

import requests


def top_ten(subreddit):
    """
        Queries the Reddit API and prints the titles of the first 10 hot posts
        listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        for i in range(10):
            print(r.json()['data']['children'][i]['data']['title'])
    else:
        print(None)
