#!/usr/bin/python3
import requests
import requests.auth

def getToken():
    client_auth = requests.auth.HTTPBasicAuth('your_id', 'your_secret')
    post_data = {"grant_type": "password", "username": "your_username", "password": "your_password"}
    headers = {"User-Agent": "Mozilla/5.0 by Jealous-Service-8067"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    res = response.json()
    token = res['access_token']
    return token
