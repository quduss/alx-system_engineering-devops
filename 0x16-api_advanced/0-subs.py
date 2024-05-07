#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit.
        None: If the subreddit does not exist or an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Python:RedditSubscriberCounter:v1.0 (by /u/user)"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data["data"]["subscribers"]
        else:
            return 0

    except Exception as e:
        return 0
