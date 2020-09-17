#!/usr/bin/python3
""" Write a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for
a given subreddit. If no results are found for the given
subreddit, the function should return None."""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """returns a list containing the titles of all hot
    articles for a given subreddit"""
    headers = {'user-agent': 'fake_user_agent'}
    base_url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)

    response = requests.get(base_url, headers=headers)

    list_posts = response.json().get('data', {}).get("children", [])
    if list_posts is None:
        if len(list_posts) == 0:
            return None
        return hot_list
    else:
        for elem in list_posts:
            hot_list.append(elem.get('data').get('title'))

    after = response.json().get('data', {}).get('after', None)
    if after is None:
        if len(list_posts) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
