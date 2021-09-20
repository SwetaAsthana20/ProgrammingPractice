def search(nums, target):
    if target > nums[-1] and target < nums[0]:
        return -1
    mini = 0
    maxi = len(nums) - 1
    while (mini <= maxi):
        mid = (mini + maxi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mini] <= nums[mid]:
            if nums[mini] <= target <= nums[mid]:
                maxi = mid - 1
            else:
                mini = mid + 1
        else:
            if nums[mid] <= target <= nums[maxi]:
                mini = mid + 1
            else:
                maxi = mid - 1
    return -1


print(search([4, 5, 6, 7, 0, 1, 2], -90475))
