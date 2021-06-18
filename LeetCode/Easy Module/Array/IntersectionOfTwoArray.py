from typing import List
import collections


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """ This method can be used only when the sequence doesn't matter in intersection."""
    counts = collections.Counter(nums1)
    res = []

    for num in nums2:
        if counts[num] > 0:
            res += num,
            counts[num] -= 1

    return res


print(intersect([9, 4, 0, 9, 5, 6, 8, 9], [9, 4, 3]))
