#!/usr/bin/python3
"""
api
"""
import sys
import requests

def recurse(subreddit, hot_list=[], after=None):
    getToken = __import__("tkn").getToken
    token = getToken()
    headers = {"Authorization": f"bearer {token}", "User-Agent": "Mozilla/5.0 by Jealous-Service-8067"}
    params = {'limit': 100, 'after': after}
    res = requests.get(f"https://oauth.reddit.com/r/{subreddit}/hot", headers=headers, allow_redirects=False, params=params)
    if res.status_code != 200:
        print("there is an error:", res.status_code)
        return None
    res = res.json()['data']
    data = res['children']
    for post in data:
        hot_list.append(post['data']['title'])

    if(res['after']):
        return(recurse(subreddit, hot_list, res['after']))

    return(hot_list);
