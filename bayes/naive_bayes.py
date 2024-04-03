import util
import random

class Classifier:
  def __init__(self, get_features):
    self.get_features = get_features
    self.cc = {}
    self.fc = {}
  def incf(self, f, cat):
    self.fc.setdefault(f, {})
    self.fc[f].setdefault(cat, 0)
    self.fc[f][cat] += 1
  def incc(self, cat):
    self.cc.setdefault(cat, 0)
    self.cc[cat] += 1
  def total_count(self):
    return sum(self.cc.values())
  def cat_count(self, cat):
    if cat in self.cc:
      return self.cc[cat]
    return 0
  def fcount(self, f, cat):
    if f in self.fc and cat in self.fc[f]:
      return self.fc[f][cat]
    return 0
  def categories(self):
    return self.cc.keys()
  def train(self, item, cat):
    features = self.get_features(item)
    for f in features:
      self.incf(f, cat)
    self.incc(cat)
  def fprob(self, f, cat):
    if self.cat_count(cat) != 0:
      return self.fcount(f, cat) / self.cat_count(cat)
    return 0

class NaiveBayesClassifier(Classifier):
  def __init__(self, get_features):
    Classifier.__init__(self, get_features)
  def prob(self, item, cat):
    cat_prob = self.cat_count(cat) / self.total_count()
    message_probability = self.message_probability(item, cat)
    return cat_prob * message_probability
  def message_probability(self, item, cat):
    features = self.get_features(item)
    p = 1
    for f in features:
      p *= self.fprob(f, cat)
    return p
  def classify(self, item):
    max_probability = 0
    best_cat = None
    for cat in self.categories():
      prob = self.prob(item, cat)
      if prob > max_probability:
        max_probability = prob
        best_cat = cat
    return best_cat

def main():
  # messages = util.get_spam_features('spambase')
  car_data = util.get_car_features('car')
  random.shuffle(car_data)
  samples = car_data[100:]
  tests = car_data[:100]
  classifier = NaiveBayesClassifier(get_features=util.get_features)
  for item in samples:
    classifier.train(item, item['outcome'])
  correct = 0
  for item in tests:
    result = classifier.classify(item)
    if result == item['outcome']:
      correct += 1
  print(f"correct: {correct} / 100")
  # random.shuffle(messages)
  # samples = messages[100:]
  # tests = messages[:100]
  # classifier = NaiveBayesClassifier(get_features=util.get_features)
  # for item in samples:
  #   classifier.train(item, item['outcome'])
  # correct = 0
  # for item in tests:
  #   result = classifier.classify(item)
  #   if result == item['outcome']:
  #     correct += 1
  # print(f"correct: {correct} / 100")

if __name__ == '__main__':
  main()