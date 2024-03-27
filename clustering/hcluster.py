import distances

class ClusterNode:
  def __init__(self, vec, left = None, right = None, distance = 0.0, id = None):
    self.left = left
    self.right = right
    self.vec = vec
    self.id = id
    self.distance = distance

def hcluster(rows, distance_measure = distances.euclidean_distance):
  distances = {}
  current_cluster_id = -1
  input_length = len(rows[0])
  clusters = [ClusterNode(rows[i], id = i) for i in range(len(rows))]
  while len(clusters) > 1:
    lowest_pair = (0, 1)
    closest_distance = distance_measure(clusters[0].vec, clusters[1].vec)
    for i in range(len(clusters)):
      for j in range(len(clusters)):
        if (clusters[i].id, clusters[j].id) not in distances:
          distances[(clusters[i].id, clusters[j].id)] = distance_measure(clusters[i].vec, clusters[j].vec)
        current_distance = distances[(clusters[i].id, clusters[j].id)]
        if current_distance < closest_distance:
          closest_distance = current_distance
          lowest_pair = (i, j)
    c0, c1 = lowest_pair
    merge_vector = [(clusters[c0].vec[i] + clusters[c1].vec[i]) / 2.0 for i in range(input_length)]
    merged_node = ClusterNode(merge_vector, left=clusters[c0], right=clusters[c1], distance=closest_distance, id=current_cluster_id)
    current_cluster_id -= 1
    del clusters[c1]
    del clusters[c0]
    clusters.append(merged_node)
  return clusters[0]