class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

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


def bfs(node):
    queue = [node]
    visited = [node.val]
    while queue:
        ele = queue.pop(0)
        for i in ele.neighbors:
            if i.val not in visited:
                queue.append(i)
                visited.append(i.val)
        print(ele.val)

print(bfs(n1))