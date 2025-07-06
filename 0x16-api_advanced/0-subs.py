#!/usr/bin/python3
"""
api
"""
import sys
import requests

def number_of_subscribers(subreddit):
    getToken = __import__("tkn").getToken
    token = getToken()
    headers = {"Authorization": f"bearer {token}", "User-Agent": "Mozilla/5.0 by Jealous-Service-8067"}
    res = requests.get(f"https://oauth.reddit.com/r/{subreddit}/about", headers=headers, allow_redirects=False)
    if res.status_code != 200:
        print("there is an error:", res.status_code)
        return

    data = res.json()['data']
    return(data['subscribers']);
