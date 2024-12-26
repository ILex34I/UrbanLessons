import numpy as np

a = np.array([1, 2, 3])

a2 = np.array([[1, 2, 3], [4, 5, 6]])
a3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(a)
# [1 2 3]

print(a2)
# [[1 2 3]
#  [4 5 6]]

print(a3)
# [[[1 2 3]
#   [4 5 6]]
#  [[7 8 9]
#   [10 11 12]]]

# Базовые функции

a = np.array([1,2,3], dtype='int32')

print(a)
# [1 2 3]

print(a.ndim)
# 1

b = np.array([[1, 2, 3], [4, 5, 6]])

print(b.ndim)
# 2

print(a.shape)
# (3,)

