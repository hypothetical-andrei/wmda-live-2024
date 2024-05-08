import numpy as np
import numpy.linalg as linalg

a = np.array([1, 2, 3, 4])

a = a.reshape((2, 2))

b = np.array([
  [2, 0],
  [0, 2]
])

print(a * b)

print(a[a>3])

print(linalg.det(a))

print(linalg.inv(a))

