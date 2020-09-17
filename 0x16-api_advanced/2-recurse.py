#!/usr/bin/python3
""" Write a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for
a given subreddit. If no results are found for the given
subreddit, the function should return None."""
import requests


def recurse(subreddit, hot_list=[]):
    """returns a list containing the titles of all hot
    articles for a given subreddit"""
    if not hot_list:
        base_url = 'https://www.reddit.com'
        headers = {'user-agent': 'fake_user_agent'}

        dict_response = requests.get(
          base_url + "/r/" + subreddit + "/hot.json",
          headers=headers,
          allow_redirects=False).json()

        list_posts = dict_response.get('data', {}).get("children", [])
        if not list_posts:
            return (None)
        else:
            return recurse(subreddit, list_posts)
    else:
        return(hot_list)
