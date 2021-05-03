def reverse(x) -> int:
    if x == 0:
        return x
    else:
        x = int(str(x)[::-1]) if x > 0 else -int(str(x)[:0:-1])
        return x if x > -1 * (2 ** 31) and x < 2 ** 31 - 1 else 0


print(reverse(-36484867))
