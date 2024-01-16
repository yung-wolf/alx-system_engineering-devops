#!/usr/bin/python3
"""
module: 1-top_ten
Holds a function - top_ten(subreddit)
"""

import requests
import sys


def top_ten(subreddit):
    """
        Queries the Reddit API and prints the titles of the first 10 hot posts
        listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    headers = {'User-Agent': agent, 'Allow-Redirects': 'false'}

    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        for i in range(10):
            print(r.json()['data']['children'][i]['data']['title'])
    else:
        print(None)


if __name__ == "__main__":
    top_ten(sys.argv[1])
