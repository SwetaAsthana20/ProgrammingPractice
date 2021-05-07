from typing import List


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def printTreeLevelOrder(root):
    if root:
        temp_queue = [root]

        while temp_queue:
            popped_root = temp_queue.pop(0)
            if popped_root.left:
                temp_queue.append(popped_root.left)
            if popped_root.right:
                temp_queue.append(popped_root.right)
            print(popped_root.value)
    return

index_preorder = 0

def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
        global index_preorder
    #if preorder[index_preorder] in inorder:
        ele = preorder[index_preorder]
        index_preorder +=1
        tree = TreeNode(ele)
        index_inorder = inorder.index(ele)
        tree.left = buildTree(preorder, inorder[:index_inorder]) if index_inorder!= 0 else None
        tree.right = buildTree(preorder, inorder[index_inorder+1:]) if index_inorder+2 <= len(inorder) else None
        return tree
    #return None





a = [3, 9, 1, 2, 20, 5, 7]
b = [1, 9, 2, 3, 5, 20, 7]
c = [1, 2]
d = [2, 1]
e = [3, 9, 20, 15, 7]
f = [9, 3, 15, 20, 7]
printTreeLevelOrder(buildTree(e, f))

