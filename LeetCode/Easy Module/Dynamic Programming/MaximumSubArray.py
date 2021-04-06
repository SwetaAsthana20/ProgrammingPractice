import math


def maxSubArray(nums) -> int:
    if len(nums) > 1:
        max_so_far, max_current = -math.inf, 0

        for i in nums:
            max_current += i
            if max_current > max_so_far:
                max_so_far = max_current

            if max_current < 0:
                max_current = 0

        return max_so_far

    return nums[0]


print(maxSubArray([3, 3, 6, -15, 9, -1, 9, -1, 0, 10]))