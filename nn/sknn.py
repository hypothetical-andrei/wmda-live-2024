from sklearn import datasets, metrics

from sklearn.neural_network import MLPClassifier

digits = datasets.load_digits()

num_samples = len(digits.images)

print(digits.images[0])

data = digits.images.reshape((num_samples, -1))

classifier = MLPClassifier(hidden_layer_sizes=(30))

train_x = data[:int(num_samples * 0.9)]
train_y = digits.target[:int(num_samples * 0.9)]

test_x =  data[int(num_samples * 0.9):]
test_y = digits.target[int(num_samples * 0.9):]

classifier.fit(train_x, train_y)

expected = test_y
predicted = classifier.predict(test_x)

print('classification report')
print(metrics.classification_report(expected, predicted))

print('confusion matrix')
print(metrics.confusion_matrix(expected, predicted))
