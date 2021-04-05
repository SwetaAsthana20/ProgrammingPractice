from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = len(nums1) - 1
    m -= 1
    n -= 1
    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[i] = nums1[m]
            m -= 1
        else:
            nums1[i] = nums2[n]
            n -= 1
        i -= 1

    if n < 0:
        return nums1
    else:
        while n >= 0:
            nums1[i] = nums2[n]
            n -= 1
            i -= 1
    return nums1


print(merge([7, 9, 13, 0, 0, 0], 3, [2, 15, 16], 3))

