def isPowerOfThree(n: int) -> bool:
    if n == 0:
        return False
    while n > 1:
        n = n / 3
    return bool(n == 1)


print(isPowerOfThree(27))