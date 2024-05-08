import numpy as np
from math import exp


x = np.array([
  [1],
  [0]
])

w = np.array([
  [0.1, 0.1],
  [0.2, 0.4]
])

b = np.array([
  [0.2],
  [0.1]
])

f = lambda x: 1 / (1 + exp(-x))

print(x * w + b)