#!/usr/bin/python3
""" Write a function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers) for a
given subreddit. If an invalid subreddit is given, the function
should return 0. """
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers (not active users, total
    subscribers) for a given subreddit.
    """
    base_url = 'https://www.reddit.com'
    headers = {'user-agent': 'fake_user_agent'}
    dict_response = requests.get(
      base_url + "/r/" + subreddit + "/about.json", headers=headers).json()
    return (dict_response.get('data', {}).get('subscribers', 0))
