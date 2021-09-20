from typing import List


def maxProduct(nums: List[int]) -> int:
    """
    There are three possibilities:
    1. minimum * curr --> max {in case of negative number}
    2. maximum * curr --> max {in case of positive number}
    3. curr --> max {when the previous value was 0}

    """

    result, maxi, mini = nums[0], nums[0], nums[0]

    for i in range(1, len(nums)):
        choice_1 = maxi * nums[i]  # taking this variable as maxi should not be updated while calculating mini
        # choice_2 = mini*nums[i]
        maxi = max(mini * nums[i], choice_1, nums[i])
        mini = min(mini * nums[i], choice_1, nums[i])

        result = max(maxi, result)

    return result


print(maxProduct([2, 2, 3, -2, 4, 8]))
