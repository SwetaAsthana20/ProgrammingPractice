from typing import List


def removingDuplicates(arr: List) -> int:
    """ We can use set() as set has property of having unique values that will remove the duplicates
    and then we can use len() method to get length of set that means number of unique element.
    """
    return len(set(arr))


def removeDups(arr: List) -> int:
    """ We can traverse the array and have a pointer that will point us to the last unique element and
     at the end we can return the pointer """
    temp = 1
    size = len(arr)
    if size == 0 or size == 1:
        return size
    for i in range(1, size):
        if arr[i] != arr[i - 1]:
            arr[temp] = arr[i]
            temp += 1
    return temp


"""Both the above method can help us in removing duplicates and return the number of unique elements in array"""
print(removingDuplicates([3, 4, 5, 6, 6, 7, 7, 8, 10]))
print(removeDups([3, 4, 5, 6, 6, 7, 7, 8, 10]))
