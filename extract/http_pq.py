import requests
from pyquery import PyQuery as pq

res = requests.get('http://andrei.ase.ro')
html = res.text
dom = pq(html)
elements = dom('a')
for element in elements:
  print(pq(element).text())
  print(pq(element).attr('href'))