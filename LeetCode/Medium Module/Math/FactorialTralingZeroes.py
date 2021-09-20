def trailingZeroes(n: int) -> int:
    count = 0

    while n > 0:
        n //= 5
        count += n

    return count


print(trailingZeroes(79))