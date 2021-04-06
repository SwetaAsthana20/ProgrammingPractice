def get_max(index, nums, dp):
    if index >= len(nums):
        return 0
    else:
        if index in dp:
            return dp[index]

        dp[index] = max(get_max(index + 1, nums, dp), nums[index] + get_max(index + 2, nums, dp))
        return dp[index]


def rob(nums) -> int:
    dp = {}
    if (len(nums)) == 1:
        return nums[0]
    return get_max(0, nums, dp)


print(rob([2, 4, 6, 1, 9, 15, 1, 0]))
