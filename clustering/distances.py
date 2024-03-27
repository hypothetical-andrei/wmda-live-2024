from math import sqrt

def euclidean_distance(v1, v2):
  sum_squares = sum([(x - y) ** 2 for (x, y) in zip(v1, v2)])
  return sqrt(sum_squares)

def main():
  sample_v1 = [1, 2, 3, 4, 5]
  sample_v2 = [2, 3, 4, 5, 6]
  print(euclidean_distance(sample_v1, sample_v2))

if __name__ == '__main__':
  main()