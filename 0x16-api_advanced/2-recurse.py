#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively collect the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of
        hot articles (default=[]).

    Returns:
        list: A list containing the titles of all hot articles
              for the subreddit.
              Returns None if no results are found or if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "MyCustomApp:v1.0"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            for post in data["data"]["children"]:
                hot_list.append(post["data"]["title"])
            if data["data"]["after"] is not None:
                # Recursive call to fetch next page of results
                recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return None

    except Exception as e:
        return None
