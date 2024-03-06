import requests

res = requests.get('http://andrei.ase.ro')
print(res.text)