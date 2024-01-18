#!/usr/bin/python3
"""
module: 0-subs
Holds function that returns the number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = requests.utils.default_headers()

    headers.update({
        'User-Agent': 'My User Agent 1.0'
    })
    r = requests.get(url, headers=headers, allow_redirects=False)
    r = r.json()
    subs = r.get('data', {}).get('subscribers')
    if subs:
        return subs
    return 0
