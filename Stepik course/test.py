import numpy as np


def make_symmetric2(matrix):
    print(matrix)
    sub = matrix.transpose()
    print(sub)
    print("----")
    print(np.tril(sub, -1))
    return np.tril(sub, -1) + matrix


matrix = np.array([[1, 2, 3, 4],
                   [0, 5, 6, 7],
                   [0, 0, 8, 9],
                   [0, 0, 0, 10]])

make_symmetric2(matrix)
a = np.zeros((3, 7))
print(a)