#!/usr/bin/python3
"""
Function to rotate matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degress in-place

    :param matrix: The input matrix to be rotated
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to get the final result
    for i in range(n - 1):
        matrix[i].reverse()

    for row in matrix:
        print(row)


if __name__ == "__main__":
    pass
