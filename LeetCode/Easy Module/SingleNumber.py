from typing import List


def singleNumber(nums: List) -> int:
    size = len(nums)
    if size == 1:
        return nums[0]
    nums.sort()
    for i in range(size):
        if i == 0 and nums[i] != nums[i + 1]:
            return nums[i]
        elif i == size - 1 and nums[i] != nums[i - 1]:
            return nums[i]
        elif nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
            return nums[i]


def singleNum(arr: List) -> int:
    temp = 0
    for i in arr:
        temp ^= i

    return temp


print(singleNum([2, 3, 4, 3, 4, 2, 0]))
print(singleNumber([2, 3, 4, 3, 4, 6, 6]))