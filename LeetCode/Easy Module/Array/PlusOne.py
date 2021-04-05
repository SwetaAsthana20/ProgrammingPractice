from typing import List


def plusOne(digits: List[int]) -> List[int]:
    if digits[-1] == 9 and len(digits) > 1:
        digits[-1] = 0
        digits[:-1] = plusOne(digits[:-1])
        return digits
    elif digits[-1] == 9 and len(digits) == 1:
        return [1, 0]
    else:
        digits[-1] = digits[-1] + 1
        return digits


print(plusOne([1, 3, 4, 5, 5, 3, 1]))

print(plusOne([1, 3, 4, 5, 5, 3, 9]))

print(plusOne([0, 3, 4, 5, 5, 3, 1]))