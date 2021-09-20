def increasingTriplet(nums) -> bool:
    count = 0
    max = nums[-1]
    min = nums[-1]
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < max:
            if nums[i] < min:
                count += 1
            min = nums[i]
        else:
            max = nums[i]
        if count == 2:
            return True
    return False


import math
def increasingTri(nums) -> bool:
    maxi = math.inf
    mini = math.inf
    for i in nums:
        if i <= mini:
            mini = i
        elif i <= maxi:
            maxi = i
        else:
            return True
    return False

print(increasingTri([1,2,3,2,1]))
