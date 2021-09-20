def findPeakElement(nums):
    if len(nums) == 1:
        return 0
    else:
        maxi = len(nums) - 1
        mini = 0
        while (mini < maxi):
            mid = (maxi + mini) // 2

            if nums[mid] > nums[mid+1]:
                maxi = mid
            else:
                mini = mid + 1
        return mini

print(findPeakElement([1,2,3,4,5,3,2,1]))