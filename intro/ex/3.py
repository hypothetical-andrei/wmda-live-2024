results = []
with open('./3.csv') as f:
  first = f.readline()
  header_items = first.strip().split(',')
  print(header_items)
  for line in f.readlines():
    line_items = line.strip().split(',')
    result = {}
    for index, item in enumerate(header_items):
      result[item] = line_items[index]
    results.append(result)
print(results)