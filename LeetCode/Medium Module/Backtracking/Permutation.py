def permute(nums):
    result = []

    def permuting(num, arr):
        if len(num) == len(nums):
            result.append(num)
        for i in range(len(arr)):
            permuting(num + [arr[i]], arr[:i] + arr[i + 1:])

    permuting([], nums)

    return result


print(permute([1, 2, 3, 4]))
