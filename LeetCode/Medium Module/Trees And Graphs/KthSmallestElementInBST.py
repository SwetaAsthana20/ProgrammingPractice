class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_in_order(root, temp):
    if root:
        if root.left:
            get_in_order(root.left, temp)
        temp.append(root.val)
        if root.right:
            get_in_order(root.right, temp)
    return temp


def kth_smallest(root: TreeNode, k: int) -> int:
    return get_in_order(root, [])[k-1]

###O(logN+k) in the average case, and O(N+k) in the worst case.
def kthSmallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right



t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(6)
t.left.left = TreeNode(2)
t.left.right = TreeNode(4)
t.left.left.left = TreeNode(1)

print(kth_smallest(t, 1))
print(kthSmallest(t, 1))