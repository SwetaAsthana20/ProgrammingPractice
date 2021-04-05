from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    if nums:
        return bool(len(nums) != len(set(nums)))
    else:
        return False


print(containsDuplicate([1, 2, 3, 4, 5, 6, 7]))
print(containsDuplicate([1, 2, 3, 4, 5, 5, 7]))
