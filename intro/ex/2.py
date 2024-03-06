results = []
with open('./2.csv') as f:
  for line in f.readlines():
    items = line.strip().split(',')
    results.append({
      'id': items[0],
      'name': items[1],
      'job': items[2]
    })
print(results)