def hammingWeight(n: int) -> int:
    result = 0
    while n:
        result += n & 1
        n = n >> 1

    return result


print(hammingWeight(9))