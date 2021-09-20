def top_k_frequent(arr, k):
    temp = {}

    for i in arr:
        if i in temp:
            temp[i] = temp[i] + 1
        else:
            temp[i] = 1

    temp_list = list(temp.values())
    temp_list.sort(reverse=True)
    temp_list[:] = temp_list[:k]

    result = []
    for i in temp_list:
        for key, value in temp.items():
            if value == i:
                result.append(key)
                temp[key] = "0"
    return result


from collections import Counter
def quick_select(arr, k):
    counts = Counter(arr)
    unique = list(counts.keys())
    n = len(unique)-1
    print(counts)

    def partition(left, right):
        pivot_index = left

        while left < right:
            while left < n and counts[unique[left]] <= counts[unique[pivot_index]]:
                left += 1

            while counts[unique[right]] > counts[unique[pivot_index]]:
                right -= 1

            if left< right:
                unique[left], unique[right] = unique[right], unique[left]
        unique[pivot_index], unique[right] = unique[right],unique[pivot_index]
        return right

    def quick_selection(left, right):

        pivot = partition(left, right)
        print(unique)

        if pivot == n-k:
            return
        elif pivot > n-k:
            return quick_selection(left, pivot-1)
        else:
            return quick_selection(pivot+1, right)

    quick_selection(0, n)
    return unique[n-k+1:]


print(quick_select([1,1,1,1,1,2,2,2,3,3,4,4,5,0,6,7,6,8,4],4))


print(top_k_frequent([1, 2], 2))
