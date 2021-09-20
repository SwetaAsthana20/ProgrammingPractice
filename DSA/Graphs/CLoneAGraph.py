class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        else:
            head = None
            temp_q = [node]
            temp_dict = {}
            while temp_q:
                ele = temp_q.pop(0)
                root = temp_dict.get(ele.val, None)
                if not root:
                    root = Node(ele.val)
                    temp_dict[ele.val] = root
                for i in ele.neighbors:
                    temp = temp_dict.get(i.val, None)
                    if not temp:
                        temp = Node(i.val)
                        temp_q.append(i)
                        temp_dict[i.val] = temp
                    root.neighbors.append(temp)
                if not head:
                    head = root
            return head


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors.append(n2)
n1.neighbors.append(n4)
n2.neighbors.append(n3)
n2.neighbors.append(n1)
n3.neighbors.append(n2)
n3.neighbors.append(n4)
n4.neighbors.append(n1)
n4.neighbors.append(n3)

s = Solution()
print(s.cloneGraph(n1))