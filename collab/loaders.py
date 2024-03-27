import os

def load_movie_lens(path = 'ml-latest-small'):
  movies = {}
  prefs = {}
  with open('.' + os.sep + path + os.sep + 'movies.csv', encoding='utf-8') as f:
    next(f)
    for line in f.readlines():
      (movie_id, title) = line.split(',')[:2]
      movies[movie_id] = title
  with open('.' + os.sep + path + os.sep + 'ratings.csv', encoding='utf-8') as f:
    next(f)
    for line in f.readlines():
      (user, movie_id, rating) = line.split(',')[:3]
      prefs.setdefault(user, {})
      prefs[user][movies[movie_id]] = float(rating)
  return prefs

def main():
  data = load_movie_lens()
  items = data.items()
  print(list(items)[:5])

if __name__ == '__main__':
  main()