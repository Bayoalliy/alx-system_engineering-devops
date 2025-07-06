#!/usr/bin/python3
"""
api
"""
import sys
import requests

def top_ten(subreddit):
    getToken = __import__("tkn").getToken
    token = getToken()
    headers = {"Authorization": f"bearer {token}", "User-Agent": "Mozilla/5.0 by Jealous-Service-8067"}
    params = {'limit': 10}
    res = requests.get(f"https://oauth.reddit.com/r/{subreddit}/hot", headers=headers, allow_redirects=False, params=params)
    if res.status_code != 200:
        print("there is an error:", res.status_code)
        return

    print(res.json()['data']['after'])
    data = res.json()['data']['children']
    for post in data:
        print(post['data']['title'])
    return(data);

top_ten('programming')
