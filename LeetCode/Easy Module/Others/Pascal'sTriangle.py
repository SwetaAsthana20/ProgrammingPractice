def generate(numRows: int):
    result = [[1]]
    for i in range(numRows - 1):
        size = len(result[-1])
        inside_temp = [result[-1][0]]
        for i in range(1, size):
            inside_temp.append(result[-1][i - 1] + result[-1][i])
        inside_temp.append(result[-1][0])
        result.append(inside_temp)

    return result


print(generate(5))