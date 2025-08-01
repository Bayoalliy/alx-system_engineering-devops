#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == '__main__':
    getToken = __import__("tkn").getToken
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{}".format(number_of_subscribers(sys.argv[1])))
