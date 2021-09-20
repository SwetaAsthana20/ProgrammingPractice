def hammingDistance(x: int, y: int) -> int:
    x ^= y
    result = 0
    while x:
        result += x & 1
        x = x >> 1

    return result

print(hammingDistance(4, 1))