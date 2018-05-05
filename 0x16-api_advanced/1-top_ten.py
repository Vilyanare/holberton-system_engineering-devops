#!/usr/bin/python3
'''
    module containing funtion top_ten
'''


def top_ten(subreddit):
    '''
        Finds top ten posts on a given subreddit and prints them
        prints none if no subreddit found
        Atrributes:
        subreddit - subreddit to find the top 10 posts of
    '''
    import requests
    url = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)
    headers = {'User-Agent': "macintosh:schoolproject (by /u/HolbertonSchool)"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        for i in r.json()['data']['children']:
            print(i['data']['title'])
    else:
        print('None')
