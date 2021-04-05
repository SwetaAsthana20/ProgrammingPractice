class Tree(object):

    def __init__(self, root, left=None, right=None):
        self.value = root
        self.left = left
        self.right = right

    def printTreeLevelOrder(self, root):
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