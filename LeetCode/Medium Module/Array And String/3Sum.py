def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)-2):
        if i == 0 or nums[i] != nums[i - 1]:
            j, k = i + 1, len(nums)-1
            while j < k:
                add = nums[j] + nums[k] + nums[i]
                if add == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif add < 0:
                    j += 1
                else:
                    k -= 1
    return result


print(threeSum([0, 0, 0, 0]))
