from Tree.TreeImpl import Tree


def maxDepth(root: Tree) -> int:
    if root is None:
        return 0
    else:
        return max(maxDepth(root.left), maxDepth(root.right)) + 1


tree = Tree(4)
tree.left = Tree(2)
tree.right = Tree(7)
tree.left.left = Tree(1)
tree.left.right = Tree(3)
tree.right.right = Tree(11)
tree.right.right.left = Tree(10)
tree.right.right.right = Tree(30)
tree.right.right.right.right = Tree(33)

print(maxDepth(tree))