def reverseBits(n: int) -> int:
    a = 0

    for i in range(32):
        t = n & 1
        a = a | t
        if i != 31:
            a = a << 1
            n = n >> 1

    return a


print(reverseBits(1))