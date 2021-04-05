from Tree.TreeImpl import Tree
from typing import List


def arrayToBST(nums: List[int]) -> Tree:
    if not nums:
        return None

    mid = (len(nums) - 1) // 2
    root = Tree(nums[mid])
    root.left = arrayToBST(nums[:mid])
    root.right = arrayToBST(nums[mid + 1:])
    return root


tree = Tree(0)
tree.printTreeLevelOrder(arrayToBST([1, 2, 3, 4, 5, 6, 7]))
