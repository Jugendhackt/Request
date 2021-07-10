import grequests

urls = [
    'https://www.reddit.com/r/mildlyinteresting.json'
]

requests = (grequests.get(u, headers = {'User-agent': 'your bot 0.1'}) for u in urls)
responses = grequests.map(requests)
jsons = (response.json() for response in responses)

print(*jsons)