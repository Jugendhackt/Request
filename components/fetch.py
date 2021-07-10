#!/bin/python3
import grequests
from posts import Post

urls = [
    'https://www.reddit.com/r/redditdev.json'
]

requests = (grequests.get(u, headers={'User-Agent': 'your bot 0.1'}) for u in urls)
responses = grequests.map(requests)
jsons = (response.json() for response in responses)

posts = []

for json in jsons:
    for post in json['data']['children']:
        posts.append(Post(post['data']['title'],
                          post['data']['url'],
                          post['data']['selftext'],
                          post['data']['author']))

print(posts)
