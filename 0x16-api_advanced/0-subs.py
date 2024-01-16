#!/usr/bin/python3
"""
module: 0-subs
Holds function that returns the number of subscribers for a given subreddit
"""


import requests
import sys


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

    headers = {
        'User-Agent': agent,
    }
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    else:
        return 0


if __name__ == "__main__":
    print(number_of_subscribers(sys.argv[1]))
