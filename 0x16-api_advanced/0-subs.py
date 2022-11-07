#!/usr/bin/python3
""" return total number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """ Queries the  Reddit API & return nUmber of subs """
    if subreddit:
        res = requests.get(
                'http://www.reddit.com/r/{}/about.json'.format(subreddit),
                headers={'User-Agent': 'Python/requests:APIproject:\
                        v1.0.0 (by /u/aaorrico23)'}).json()

        sub = res.get("data", {}).get("subscribers", 0)
        return sub
    return 0
