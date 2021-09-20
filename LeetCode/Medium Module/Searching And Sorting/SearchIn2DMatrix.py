def search_matrix(matrix, target):
    def get_num(m, n):
        mini = 0
        maxi = n - 1
        while mini <= maxi:
            mid = (mini + maxi) // 2

            if matrix[m][mid] == target:
                return True
            elif matrix[m][mid] > target:
                maxi = mid - 1
            else:
                mini = mid + 1

        mini = 0
        maxi = m - 1

        while mini <= maxi:
            mid = (mini + maxi) // 2

            if matrix[mid][n] == target:
                return True
            elif matrix[mid][n] > target:
                maxi = mid - 1
            else:
                mini = mid + 1

        return False

    n = len(matrix)
    m = len(matrix[0])
    result = False
    if n and m:

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if result:
                return result
            if matrix[i][j] == target:
                return True
            elif target < matrix[i][j] and target >= matrix[0][j] or target >= matrix[i][0]:
                result = get_num(i, j)
            i -= 1
            j -= 1
    return result


print(search_matrix([[1,4,7,11,15],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 15))