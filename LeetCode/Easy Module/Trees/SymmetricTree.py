from Tree.TreeImpl import Tree


def isSymmetric(root: Tree) -> bool:
    def check(lefty, righty):
        if lefty and righty:
            if lefty.value != righty.value:
                return False
            return check(lefty.left, righty.right) and check(lefty.right, righty.left)

        if (not lefty and righty) or (not righty and lefty):
            return False
        return True
    return check(root.left, root.right)


tree = Tree(4)
tree.left = Tree(2)
tree.right = Tree(2)
tree.left.left = Tree(1)
tree.left.right = Tree(3)
tree.right.right = Tree(1)
tree.right.left = Tree(3)

print(isSymmetric(tree))
