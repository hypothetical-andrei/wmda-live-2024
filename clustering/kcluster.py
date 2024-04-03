import loaders
import distances
import random
from sklearn.datasets import load_iris

def kclusters(rows, cluster_count=4, distance=distances.euclidean_distance):
  MAX_ITER = 100
  feature_count = len(rows[0])
  intervals = [(min([row[i] for row in rows]), max([row[i] for row in rows])) for i in range(feature_count)]
  clusters = [[random.random() * (intervals[i][1] - intervals[i][0]) + intervals[i][0] for i in range(feature_count)] for j in range(cluster_count)]
  last_matches = None
  for t in range(MAX_ITER):
    best_matches = [[] for i in range(cluster_count)]
    for j in range(len(rows)):
      current_row = rows[j]
      best_match = 0
      for i in range(cluster_count):
        d = distance(clusters[i], current_row)
        if d < distance(clusters[best_match], current_row):
          best_match = i
      best_matches[best_match].append(j)
    if best_matches == last_matches:
      break
    for i in range(cluster_count):
      avgs = [0.0] * feature_count
      if len(best_matches[i]) > 0:
        for row_id in best_matches[i]:
          for j in range(feature_count):
            avgs[j] += rows[row_id][j]
        for j in range(feature_count):
          avgs[j] /= len(best_matches[i])
        clusters[i] = avgs
    last_matches = best_matches
  return best_matches

def main():
  MAX_CLUSTERS = 3
  # col_names, row_names, data = loaders.load_blog_data()
  # clusters = kclusters(data, cluster_count = MAX_CLUSTERS)
  # print(clusters)
  data = load_iris()
  # print(data)
  clusters = kclusters(data.data, cluster_count = MAX_CLUSTERS)
  # print(clusters)
  cluster_structure = []
  for cluster in clusters:
    cluster_structure.append((
      len([x for x in cluster if data.target[x] == 0]),
      len([x for x in cluster if data.target[x] == 1]),
      len([x for x in cluster if data.target[x] == 2])
    ))
  cluster_purities = [max(x)/sum(x) for x in cluster_structure]
  print(cluster_purities)

if __name__ == '__main__':
  main()