import loaders
import distances
import random
from sklearn.datasets import load_iris
from PIL import Image, ImageDraw
from math import sqrt

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

# def adjust(data, distance = distances.euclidean_inverse, rate = 0.01):
#   n = len(data)
#   real_dist = [[distance(data[i], data[j]) for j in range(n)] for i in range(n)]
#   fake_dist = [[0.0 for j in range(n)] for i in range(n)]
#   loc = [[random.random(), random.random()] for i in range(n)]
#   last_error = None
#   MAX_EPOCHS = 1000
#   for t in range(MAX_EPOCHS):
#     for i in range(n):
#       for j in range(n):
#         fake_dist[i][j] = sqrt(sum([(loc[i][x] - loc[j][x]) ** 2 for x in range(len(loc[i]))]))
#       grad = [[0.0, 0.0] for i in range(n)]
#       total_error = 0
#       for i in range(n):
#         for j in range(n):
#           if i == j:
#             continue
#           current_error = (fake_dist[j][i] - real_dist[j][i]) / real_dist[j][i]
#           grad[i][0] = current_error * (loc[j][0] - loc[i][0]) / fake_dist[i][j]
#           grad[i][1] = current_error * (loc[j][1] - loc[i][1]) / fake_dist[i][j]
#           total_error += current_error
#       if last_error and last_error < total_error:
#         break
#       last_error = total_error
#       for i in range(n):
#         loc[i][0] = rate * grad[i][0]
#         loc[i][1] = rate * grad[i][1]
#   return loc

def adjust(data, distance = distances.euclidean_inverse, rate = 0.01):
  n = len(data)
  realdist = [[distance(data[i], data[j]) for j in range(n)] for i in range(n)]
  fakedist = [[0.0 for j in range(n)] for i in range(n)]
  loc = [[random.random(), random.random()] for i in range(n)]
  lasterror = None
  for t in range(1000):
    for i in range(n):
      for j in range(n):
        fakedist[i][j] = sqrt(sum([pow(loc[i][x] - loc[j][x], 2) for x in range(len(loc[i]))]))
  
    grad = [[0.0, 0.0] for i in range(n)]
    totalerror = 0
    for i in range(n):
      for j in range(n):
        if i == j:
          continue
        errorterm = (fakedist[j][i] - realdist[j][i]) / realdist[j][i]
        grad[i][0] = errorterm * (loc[j][0] - loc[i][0]) / fakedist[i][j] 
        grad[i][1] = errorterm * (loc[j][1] - loc[i][1]) / fakedist[i][j]
        totalerror += errorterm
    if lasterror and lasterror < totalerror:
      break
    lasterror = totalerror
    for i in range(n):
      loc[i][0] -= grad[i][0] * rate
      loc[i][1] -= grad[i][1] * rate

  return loc

def draw2d(data, labels, jpeg='kcluster.jpg'):
  img = Image.new('RGB', (2000, 2000), (255, 255, 255))
  draw = ImageDraw.Draw(img)
  for i in range(len(data)):
    x = (data[i][0] + 0.5) * 1000
    y = (data[i][1] + 0.5) * 1000
    draw.text((x, y), labels[i], (0, 0, 0))
  img.save(jpeg, 'JPEG')

def main():
  MAX_CLUSTERS = 3
  col_names, row_names, data = loaders.load_blog_data()
  # clusters = kclusters(data, cluster_count = MAX_CLUSTERS)
  # print(clusters)
  data = load_iris()
  coords = adjust(data.data)
  draw2d(coords, labels = [f"{data.target_names[x]}" for x in data.target])
  # print(data)
  # clusters = kclusters(data.data, cluster_count = MAX_CLUSTERS)
  # print(clusters)
  # cluster_structure = []
  # for cluster in clusters:
  #   cluster_structure.append((
  #     len([x for x in cluster if data.target[x] == 0]),
  #     len([x for x in cluster if data.target[x] == 1]),
  #     len([x for x in cluster if data.target[x] == 2])
  #   ))
  # cluster_purities = [max(x)/sum(x) for x in cluster_structure]
  # print(cluster_purities)

if __name__ == '__main__':
  main()