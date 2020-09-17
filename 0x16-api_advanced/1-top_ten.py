#!/usr/bin/python3
""" Write a function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers) for a
given subreddit. If an invalid subreddit is given, the function
should return 0. """
import requests


def top_ten(subreddit):
    """Returns the number of subscribers (not active users,
    total subscribers) for a given subreddit."""
    base_url = 'https://www.reddit.com'
    headers = {'user-agent': 'fake_user_agent'}

    dict_response = requests.get(
      base_url + "/r/" + subreddit + "/hot.json",
      headers=headers,
      allow_redirects=False).json()

    list_posts = dict_response.get('data', {}).get("children", [])
    if not list_posts:
        print("None")
    # for dict_elem in list_children:
    #     final_dict[dict_elem.get('data').get('title')] = dict_elem.get(
    #       'data').get('ups')

    # list_sorted = sorted(final_dict.items(),
    # key=lambda x: x[1], reverse=True)
    for title in list_posts[:10]:
        print(title.get('data').get('title'))
