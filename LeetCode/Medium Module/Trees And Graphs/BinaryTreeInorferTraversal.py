from typing import List

class TreeNode:
    def __init__(self,value , left= None, right= None):
        self.value = value
        self.left = left
        self.right = right


def get_inorder(root, temp_list):
    if not root:
        return
    get_inorder(root.left, temp_list)
    temp_list.append(root.value)
    get_inorder(root.right, temp_list)
    return temp_list

def inorderTraversal(root: TreeNode) -> List[int]:
    return get_inorder(root , [])


t = TreeNode(3)
t.left = TreeNode(4)
t.right = TreeNode(7)
t.left.left = TreeNode(9)
t.left.right = TreeNode(10)

print(inorderTraversal(t))