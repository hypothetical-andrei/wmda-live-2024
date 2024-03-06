import requests
import json

template = 'http://sg.media-imdb.com/suggests/{first}/{start}.json'
url = template.format(first = 'a', start='ab')
response = requests.get(url)
jsonpData = response.text
data = jsonpData[8:-1]
recommendations = json.loads(data)
for item in recommendations['d']:
  if item['s'].startswith('Act'):
    print(item['l'])