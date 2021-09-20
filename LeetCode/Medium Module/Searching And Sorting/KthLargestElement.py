def partition(arr, low, high, pivot):
    while low < high:

        while low < len(arr) and arr[low] <= arr[pivot]:
            low += 1

        while arr[high] > arr[pivot]:
            high -= 1

        if low < high:
            arr[low], arr[high] = arr[high], arr[low]

    arr[pivot], arr[high] = arr[high], arr[pivot]

    return high


def k_largest(arr, k, n, low, high):
    pivot = partition(arr, low, high, low)

    if pivot > n - k:
        return k_largest(arr, k, n, low, pivot - 1)
    elif pivot < n - k:
        return k_largest(arr, k, n, pivot + 1, high)
    else:
        return arr[pivot]


a = [8, 3, 5, 0, 7, 4, 2, 9, 6, 4]

print(k_largest(a, 4, len(a), 0, len(a) - 1))

