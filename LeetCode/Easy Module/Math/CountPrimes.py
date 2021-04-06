def countPrimes(n: int) -> int:
    temp = [1 for i in range(n)]
    i = 2
    count = 0
    while i * i < n:
        if temp[i] == 1:
            for j in range(i * i, n, i):
                temp[j] = 0
        i += 1

    for i in range(2, n):
        if temp[i] == 1:
            count += 1

    return count


print(countPrimes(9))