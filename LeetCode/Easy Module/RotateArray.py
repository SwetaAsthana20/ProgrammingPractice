from typing import List


def rotate(arr: List, k: int) -> List:
    size = len(arr)
    k = k % size

    if size != 0 and size != 1 and k != 0 and k != size:
        arr[:] = arr[-k:] + arr[:-k]

    return arr

def rotation(arr: List, k: int) -> List:
    size = len(arr)
    k = k % size

    if size == 0 or size == 1 or k == 0 or k == size:
        return arr

    temp = arr[-k:]

    for i in range(size-k-1,-1,-1):
        arr[i+k] = arr[i]

    size = len(temp)
    for i in range(size):
        arr[i] = temp[i]

    return arr


print(rotate([1, 5, 3, 5, 7, 9], 2))
print(rotate([1, 3, 5, 7, 8, 3, 8], 9))