import data_sample
from math import sqrt
from scipy.stats import pearsonr

def euclidean_distance(prefs, me, other):
  shared = {}
  for item in prefs[me]:
    if item in prefs[other]:
      shared[item] = 1
  if len(shared) == 0:
    return 0
  square_sum = sum([pow(prefs[me][item] - prefs[other][item], 2) for item in prefs[me] if item in prefs[other]])
  return 1 / sqrt(1 + square_sum)

def pearson_correlation(prefs, me, other):
  shared = {}
  for item in prefs[me]:
    if item in prefs[other]:
      shared[item] = 1
  if len(shared) == 0:
    return 0
  my_ratings = [prefs[me][item] for item in shared]
  other_ratings = [prefs[other][item] for item in shared]
  return pearsonr(my_ratings, other_ratings)

def main():
  data = data_sample.critics
  print(euclidean_distance(data, 'Mick LaSalle', 'Jack Matthews'))
  print(pearson_correlation(data, 'Mick LaSalle', 'Jack Matthews'))

if __name__ == '__main__':
  main()