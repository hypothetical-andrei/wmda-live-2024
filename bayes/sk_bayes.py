from sklearn.naive_bayes import GaussianNB
import util

def main():
  messages = util.get_spam_features_sk('spambase')
  samples = messages[100:]
  tests = messages[:100]
  sample_features = [item['features'] for item in samples]
  sample_outcomes = [item['outcome'] for item in samples]
  classifier = GaussianNB()
  classifier.fit(sample_features, sample_outcomes)
  test_features = [item['features'] for item in tests]
  test_outcomes = [item['outcome'] for item in tests]
  predicted = classifier.predict(test_features)
  correct = len([item for item in zip(test_outcomes, predicted) if item[0] == item[1]])
  print(f"correct: {correct}/100")

if __name__ == '__main__':
  main()