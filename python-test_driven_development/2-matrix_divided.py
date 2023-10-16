#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    0- matrix must be a list of lists of integers or floats
    1- Each row of the matrix must be of the same size
    2- div must be a number (integer or float)
    3- div can not be equal to 0
    """
    if type(div) not in (int, float):
        raise ValueError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(
        isinstance(row, list) and
            all(isinstance(val, (int, float)) for val in row)
            for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    result = [[round(cell / div, 2) for cell in row] for row in matrix]

    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
