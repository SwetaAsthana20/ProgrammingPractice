from typing import List
from Tree.TreeImpl import Tree


def levelOrder(root: Tree) -> List[List[int]]:
    result = []
    if root:
        temp_queue = [root]
        temp_list = []
        counter = 1
        while temp_queue:

            temp = temp_queue.pop(0)
            if temp.left:
                temp_queue.append(temp.left)
            if temp.right:
                temp_queue.append(temp.right)

            temp_list.append(temp.value)
            counter -= 1
            if counter == 0:
                result.append(temp_list)
                temp_list = []
                counter = len(temp_queue)
    return result


tree = Tree(4)
tree.left = Tree(2)
tree.right = Tree(7)
tree.left.left = Tree(1)
tree.left.right = Tree(3)
tree.right.right = Tree(11)
tree.right.right.left = Tree(10)
tree.right.right.right = Tree(30)
tree.right.right.right.right = Tree(33)


print(levelOrder(tree))
