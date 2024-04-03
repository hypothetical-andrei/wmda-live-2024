import distances
import loaders
from PIL import Image, ImageDraw
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
      for j in range(i+1, len(clusters)):
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

def print_cluster(node, labels=None, n=0):
  for i in range(n):
    print(' ', end='')
  if node.id < 0:
    print('+')
  else:
    if labels == None:
      print(node.id)
    else:
      print(labels[node.id])
  if node.left != None:
    print_cluster(node.left, labels=labels, n=n+1)
  if node.right != None:
    print_cluster(node.right, labels=labels, n=n+1)

def get_height(cluster):
  if cluster.left == None and cluster.right == None:
    return 1
  else:
    return get_height(cluster.left) + get_height(cluster.right)

def get_depth(cluster):
  if cluster.left == None and cluster.right == None:
    return 0
  return max(get_depth(cluster.left), get_depth(cluster.right)) + cluster.distance

def draw_node(draw, cluster, x, y, scaling, labels):
  if cluster.id < 0:
    hl = get_height(cluster.left) * 20
    hr = get_height(cluster.right) * 20
    top = y - (hl + hr) / 2
    bottom = y + (hl + hr) / 2
    line_length = cluster.distance * scaling
    draw.line((x, top + hl / 2, x, bottom - hr / 2 ), fill=(255, 0, 0))
    draw.line((x, top + hl / 2, x + line_length, top + hl / 2 ), fill=(255, 0, 0))
    draw.line((x, bottom - hr / 2, x + line_length, bottom - hr / 2 ), fill=(255, 0, 0))
    draw_node(draw, cluster.left, x + line_length, top + hl / 2, scaling, labels)
    draw_node(draw, cluster.right, x + line_length, bottom - hr / 2, scaling, labels)
  else:
    draw.text((x + 5, y - 7), labels[cluster.id], (0, 0, 0))

def draw_tree(cluster, labels, jpeg='hcluster.jpg'):
  h = get_height(cluster) * 20
  w = 1200
  depth = get_depth(cluster)
  scaling = float(w - 300) / depth
  img = Image.new('RGB', (w, h), (255, 255, 255))
  draw = ImageDraw.Draw(img)
  draw.line((0, h / 2, 10, h / 2), fill=(255, 0, 0))
  draw_node(draw, cluster, 10, h / 2, scaling, labels)
  img.save(jpeg, 'JPEG')

def main():
  col_name, row_names, data = loaders.load_blog_data()
  root = hcluster(data)
  print_cluster(root, labels=row_names)
  # print_cluster(root)
  draw_tree(root, labels=row_names)

if __name__ == '__main__':
  main()