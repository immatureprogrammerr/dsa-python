def rotate_matrix_by_90(matrix):
    n = len(matrix)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
    
    # reverse can be done using slicing as well
    # matrix = [row[::-1] for row in matrix]

    return matrix

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

rotated_matrix = rotate_matrix_by_90(matrix)
print(rotated_matrix)