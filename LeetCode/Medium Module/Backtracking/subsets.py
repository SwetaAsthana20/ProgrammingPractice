def subsets(arr):
    result = [[], ]

    def get_subset(item, pos, length):
        if len(item) == length:
            return result.append(item)
        for i in range(pos, len(arr)):
            get_subset(item + [arr[i]], i + 1, length)

    for j in range(len(arr)):
        get_subset([], 0, j + 1)

    return result


def subsets1(nums):
    def backtrack(start, cur_list):
        ans.append(cur_list[:])

        for j in range(start, n):
            cur_list.append(nums[j])
            backtrack(j + 1, cur_list)
            cur_list.pop()

    n = len(nums)
    ans = []

    backtrack(0, [])

    return ans


print(subsets1([1, 2, 3, 4]))
