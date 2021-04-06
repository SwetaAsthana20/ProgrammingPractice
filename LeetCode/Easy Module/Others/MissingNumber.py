def missingNumber(nums) -> int:
    n = len(nums)
    sums = (n * (n + 1)) // 2
    sumn = sum(nums)

    return sums - sumn


print(missingNumber([5, 2, 1, 3, 0]))
