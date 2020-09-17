#!/usr/bin/python3
# from sys import argv
import requests


def number_of_subscribers(subreddit):
    base_url = 'https://www.reddit.com'
    headers = {'user-agent': 'fake_user_agent'}
    dict_response = requests.get(
      base_url + "/r/" + subreddit + "/about.json", headers=headers).json()
    return (dict_response.get('data', {}).get('subscribers', 0))
