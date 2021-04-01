def rotate(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    temp = {}
    size = len(matrix)

    for i in range(size):
        for j in range(size):
            changed_index = "%d,%d" % (j, -1 * (i + 1))
            current_index = "%d,%d" % (i, -1 * (size - j))
            if current_index in temp:
                value = temp[current_index]
            else:
                value = matrix[i][-1 * (size - j)]

            temp[changed_index] = matrix[j][-1 * (i + 1)]
            matrix[j][-1 * (i + 1)] = value
    return matrix


def rotateIsEqualTOTransposeAndReverse(mat):
    size = len(mat)

    for i in range(size):  # REVERSE
        for j in range(size//2):
            mat[i][j], mat[i][-j - 1] = mat[i][-j - 1], mat[i][j]

    for i in range(size):  # TRANSPOSE
        for j in range(i,size):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    return mat


print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
print(rotateIsEqualTOTransposeAndReverse([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))