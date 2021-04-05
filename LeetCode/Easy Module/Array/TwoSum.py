from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    temp = {}

    for i in range(len(nums)):
        try:
            return temp[target - nums[i]], i
        except:
            pass
        temp[nums[i]] = i


print(twoSum([2, 3, 5, 7, 3, 5, 7, 5], 6))
