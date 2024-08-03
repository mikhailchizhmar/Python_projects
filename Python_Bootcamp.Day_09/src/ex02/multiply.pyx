cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def mul(a, b):
    cdef int i, j, k

    if len(a) == 0 or len(b) == 0:
        raise ValueError("Input matrices cannot be empty.")

    for row in a:
        if not isinstance(row, list):
            raise TypeError("Both arguments must be lists of lists of integers.")
        for elem in row:
            if not isinstance(elem, int):
                raise TypeError("Both arguments must be lists of lists of integers.")

    for row in b:
        if not isinstance(row, list):
            raise TypeError("Both arguments must be lists of lists of integers.")
        for elem in row:
            if not isinstance(elem, int):
                raise TypeError("Both arguments must be lists of lists of integers.")

    cdef int rows_a = len(a)
    cdef int cols_a = len(a[0])
    cdef int cols_b = len(b[0])

    if cols_a != len(b):
        raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")

    cdef list result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result