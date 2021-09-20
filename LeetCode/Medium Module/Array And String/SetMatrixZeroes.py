def set_flag(row, col, matrix, row_size, col_size):
    for i in range(row_size):
        if matrix[i][col] != 0:
            matrix[i][col] = '-1'
    for i in range(col_size):
        if matrix[row][i] != 0:
            matrix[row][i] = '-1'

    return matrix

def setZeroe(matrix):
    row_size = len(matrix)
    col_size = len(matrix[0])

    for i in range(row_size):
        for j in range(col_size):
            if matrix[i][j] == 0:
                matrix = set_flag(i, j, matrix, row_size, col_size)

    for i in range(row_size):
        for j in range(col_size):
            if matrix[i][j] == '-1':
                matrix[i][j] = 0

    return matrix

def set_Zeroes(matrix):
    row_size = len(matrix)
    col_size = len(matrix[0])
    is_Zero_in_Col = False

    for i in range(row_size):
        if matrix[i][0] == 0:
            is_Zero_in_Col = True
        for j in range(1, col_size):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, row_size):
        for j in range(1, col_size):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for i in range(col_size):
            matrix[0][i] = 0

    if is_Zero_in_Col:
        for i in range(row_size):
            matrix[i][0] = 0

    return matrix


print(set_Zeroes([[1,7,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]))
