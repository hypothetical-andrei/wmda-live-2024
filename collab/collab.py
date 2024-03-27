import data_sample
import distances
import transform
import json
from json.decoder import JSONDecodeError
from loaders import load_movie_lens

def top_matches(prefs, me, n = 5, similarity=distances.euclidean_distance):
  scores = [(similarity(prefs, me, other), other) for other in prefs if other != me]
  scores.sort()
  scores.reverse()
  return scores[:n]

def get_recommendations(prefs, me, n = 5, similarity=distances.euclidean_distance):
  totals = {}
  similarity_sums = {}
  for other in prefs:
    if other == me:
      continue
    sim = similarity(prefs, me , other)
    if sim == 0:
      continue
    for item in prefs[other]:
      if item not in prefs[me]:
        totals.setdefault(item, 0)
        totals[item] = totals[item] + prefs[other][item] * sim
        similarity_sums.setdefault(item, 0)
        similarity_sums[item] = similarity_sums[item] + sim
  rankings = [(total/similarity_sums[item], item) for item, total in totals.items()]
  rankings.sort()
  rankings.reverse()
  return rankings[:n]

def get_similar_items(prefs, n=5, similarity=distances.euclidean_distance):
  result = {}
  for item in prefs:
    result[item] = top_matches(prefs, item, similarity=similarity)
  return result

def get_recommended_items(prefs, item_similarities, me):
  my_ratings = prefs[me]
  scores = {}
  totals = {}
  for item, rating in my_ratings.items():
    for sim, other_item in item_similarities[item]:
      if other_item in prefs[me]:
        continue
      scores.setdefault(other_item, 0)
      scores[other_item] = scores[other_item] + sim * rating
      totals.setdefault(other_item, 0)
      totals[other_item] = totals[other_item] + sim
  rankings = [(score/totals[item], item) for item, score in scores.items()]
  rankings.sort()
  rankings.reverse()
  return rankings

def main():
  # data = data_sample.critics
  data = load_movie_lens()
  # print(top_matches(data, 'Toby', n = 3))
  # recommendations = get_recommendations(data, 'Toby', n = 3)
  # print(recommendations)
  item_data = transform.tranform_prefs(data)
  try:
    with open('items.json') as f:
      item_similarities = json.loads(f.read())
  except (FileNotFoundError, JSONDecodeError):
    item_similarities = get_similar_items(item_data)
    with open('items.json', 'w') as f:
      f.write(json.dumps(item_similarities))
  print(get_recommended_items(data, item_similarities, '489'))

if __name__ == '__main__':
  main()