#!/usr/bin/python3
"""
api
"""
import sys
import requests

def count_words(subreddit, word_list, after=None, dic={}):
    getToken = __import__("tkn").getToken
    token = getToken()
    headers = {"Authorization": f"bearer {token}",
                "User-Agent": "Mozilla/5.0 by Jealous-Service-8067"}
    params = {'limit': 100, 'after': after}
    res = requests.get(f"https://oauth.reddit.com/r/{subreddit}/hot",
                        headers=headers, allow_redirects=False,
                        params=params)
    if res.status_code != 200:
        return None
    res = res.json()['data']
    data = res['children']
    for post in data:
        post_title = post['data']['title']
        for t_word in post_title.lower().split():
            for l_word in " ".join(word_list).lower().split():
                if t_word == l_word:
                    if dic.get(t_word):
                        dic[t_word] += 1
                    else:
                        dic[t_word] = 1

    if(res['after']):
        return(count_words(subreddit, word_list, res['after'], dic))

    sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    for key, value in sorted_dict.items():
        print(key + ': ' + str( value))
    return
