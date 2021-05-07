from typing import List


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def zigzag_level_order(root: TreeNode) -> List[List[int]]:
    result = []
    if root:
        counter = 1
        temp_list = [root]
        temp = []
        flag = True
        while temp_list:
            ele = temp_list.pop(0)
            if ele.left:
                temp_list.append(ele.left)
            if ele.right:
                temp_list.append(ele.right)

            temp.append(ele.value)
            if len(temp) == counter:
                if flag:
                    result.append(temp)
                else:
                    result.append(temp[::-1])
                flag = not flag
                temp = []
                counter = len(temp_list)

    return result


t = TreeNode(3)
t.left = TreeNode(4)
t.right = TreeNode(20)
t.right.left = TreeNode(5)
t.right.right = TreeNode(7)

t = TreeNode(3)
t.left = TreeNode(4)
t.right = TreeNode(20)
t.right.left = TreeNode(5)
t.right.right = TreeNode(7)

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)

print(zigzag_level_order(t))
