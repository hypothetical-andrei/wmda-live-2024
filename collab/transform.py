import data_sample

def tranform_prefs(prefs):
  result = {}
  for person in prefs:
    for item in prefs[person]:
      result.setdefault(item, {})
      result[item][person] = prefs[person][item]
  return result

def main():
  data = data_sample.critics
  print(tranform_prefs(data))

if __name__ == '__main__':
  main()