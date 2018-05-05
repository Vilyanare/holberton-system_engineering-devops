#!/usr/bin/python3
'''
    module containing the recurse function
'''
import requests


def recurse(subreddit, hot_list=[]):
    '''
        function that recursively finds a list of all hot topics of a subreddit
        Attributes:
        subreddit - subreddit to find hot topics of
        hot_list - list to store topics in

        Returns: list of hot topics or None if subreddit not found
    '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': "macintosh:schoolproject (by /u/HolbertonSchool)"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        recurse_helper(subreddit, hot_list)
        return hot_list
    else:
        return None


def recurse_helper(subreddit, hot_list, after=""):
    '''
        Helper function to do recursion after data is valid
        Attributes:
        subreddit - subreddit to query
        hot_list - list to store topic titles
        after - where to start url query
        count - how many titles have already been returned

        Returns: hot_list populated with titles
    '''
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
        subreddit, after, count)
    headers = {'User-Agent': "macintosh:schoolproject (by /u/HolbertonSchool)"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    new_after = r.json()['data']['after']
    if new_after is not None:
        recurse_helper(subreddit, hot_list, new_after)
    for i in r.json()['data']['children']:
        hot_list.append(i['data']['title'])
