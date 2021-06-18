class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def printTreeLevelOrder(root):
    if root:
        temp_queue = [root]

        while temp_queue:
            popped_root = temp_queue.pop(0)
            if popped_root.left:
                temp_queue.append(popped_root.left)
            if popped_root.right:
                temp_queue.append(popped_root.right)
            print(popped_root.val,"-->",popped_root.next.val if popped_root.next else None)
    return


def insert_child(curr, temp):
    if curr.left:
        temp.append(curr.left)
    if curr.right:
        temp.append(curr.right)
    return temp


def connect(root: 'Node') -> 'Node':
    temp = [root]
    count = 1
    while temp:
        curr = temp.pop(0)
        count -= 1
        if count == 0:
            curr.next = None
            temp = insert_child(curr, temp)
            count = len(temp)
        else:
            curr.next = temp[0]
            temp = insert_child(curr, temp)
    return root


def connect_bst(root: 'Node') -> 'Node':
    leftmost = root

    while leftmost.left:
        head = leftmost
        while head:
            head.left.next = head.right

            if head.next:
                head.right.next = head.next.left

            head = head.next

        leftmost = leftmost.left

    return root






t = Node(1)
t.left = Node(2)
t.right = Node(3)
t.left.left = Node(4)
t.left.right = Node(5)
t.right.left = Node(6)
t.right.right = Node(7)

#print(printTreeLevelOrder(connect(t)))
print("*****************************")
print(printTreeLevelOrder(connect_bst(t)))