def get_car_data(filename = 'car.data'):
  results = []
  with open(filename) as f:
    for line in f.readlines():
      items = line.strip().split(',')
      results.append(items)
  return results

def main():
  items = get_car_data()
  print(items[:5])

if __name__ == '__main__':
  main()