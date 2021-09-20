def get_index(index, flag, nums):
    while flag == "start" and index > 0 and nums[index] == nums[index - 1]:
        index -= 1
    while flag == "end" and index < len(nums) - 1 and nums[index] == nums[index + 1]:
        index += 1
    return index


def search_for_a_range(nums, target):
    maxi = len(nums) - 1
    mini = 0

    while (mini < maxi):
        mid = (maxi + mini) // 2
        if nums[mid] > target:
            maxi = mid
        elif nums[mid] < target:
            mini = mid + 1
        else:
            start = get_index(mid, "start", nums)
            end = get_index(mid, "end", nums)
            return [start, end]
    if nums[-1] == target:
        return [len(nums)-1, len(nums)-1]

    return [-1, -1]


def searchRange(nums, target):
    def binarySearchLeft(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if x > A[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def binarySearchRight(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if x >= A[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
    return (left, right) if left <= right else [-1, -1]


print(search_for_a_range([1], 1))
print(searchRange([5,7,7,8,8,10,11], 8))
