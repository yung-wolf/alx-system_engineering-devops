#!/usr/bin/python3
"""
module: 2-recurse
Holds one function
recurse(subreddit, hot_list=[], after=None, limit=100, count=0)
"""
import requests


def recurse(subreddit, hot_list=[], after=None, limit=100, count=0):
    """
        Queries the Reddit API and returns a list containing the titles of all
          hot articles for a given subreddit.
        If no results are found for the given subreddit,
          the function should return None.

        :param subreddit: subreddit to search
        :param hot_list: list of titles of all hot articles for a
          given subreddit
        :param after: parameter for the next page
        :param limit: maximum number of posts retrieved
        :param count: number of posts retrieved
        :return:
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    # Get copy of default headers that requests would use
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    # Get the response from the API
    if after is not None:
        url = url + '?after={}'.format(after)

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code == 200:
        data = r.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            return hot_list  # No more posts to retrieve

        titles = [post['data']['title'] for post in posts]
        hot_list.extend(titles)

        # Recursively call the function with the new 'after' parameter
        after = data.get('data', {}).get('after')
        if not after:
            return hot_list
        count += len(posts)
        return recurse(subreddit, hot_list, after, limit, count)

    else:
        return None
