#!/usr/bin/python3
'''
    module holding the function number_of_subscribers
'''


def number_of_subscribers(subreddit):
    '''
        Function to find number of subscribers to a specified subreddit
        Arguments:
        subreddit - subreddit to check subs for

        Returns: how many subscribers or 0 if subreddit not found
    '''
    import requests
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': "macintosh:schoolproject (by /u/HolbertonSchool)"}
    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code == 200:
        return r.json()['data']['subscribers']
    else:
        return 0
