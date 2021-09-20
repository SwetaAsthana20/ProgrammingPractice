from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zero_pointer = 0
    size = len(nums)
    for i in range(size):
        if nums[i] != 0:
            nums[i], nums[zero_pointer] = nums[zero_pointer], nums[i]
            zero_pointer += 1
    return nums


print(moveZeroes([1, 0, 3, 5, 0, 5, 6, 9, 0, 7, 0, 70, 0, 0, 0, 0]))
