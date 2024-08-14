#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    # Dfine the URL for the subreddit about.json endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests error
    user_agent = "python:subreddit.subscriber.counter:v1.0 (by u/yourusername)"
    headers = {"User-Agent": user_agent}

    # Make the request without following redirects
    reponse = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            return data.get('subscribers', 0)
    # If the subreddit is invalid or any other issue, return 0
    return 0
