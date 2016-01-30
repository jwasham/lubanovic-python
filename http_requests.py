import requests
import json

url = 'http://api.icndb.com/jokes/random'
resp = requests.get(url)

# print(resp.status_code)
# print(resp.text)

if resp.status_code == 200:
    jokeObj = json.loads(resp.text)
    print(jokeObj['value']['joke'])
else:
    raise Exception("I failed to get the joke.")
