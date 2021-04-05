from Tree.TreeImpl import Tree
import math


def checkingBST(root, maxi, mini):
    if root is None:
        return True
    else:
        if root.value >= maxi or root.value <= mini:
            return False
        else:
            return checkingBST(root.right, maxi, root.value) and checkingBST(root.left, root.value, mini)


def isValidBST(root: Tree) -> bool:
    return checkingBST(root, math.inf, -math.inf)


tree = Tree(4)
tree.left = Tree(2)
tree.right = Tree(7)
tree.left.left = Tree(1)
tree.left.right = Tree(3)
tree.right.right = Tree(11)
tree.right.right.left = Tree(10)
tree.right.right.right = Tree(30)
tree.right.right.right.right = Tree(33)

print(isValidBST(tree))
