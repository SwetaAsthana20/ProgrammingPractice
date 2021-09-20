class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Codec:

    def serialize(self, root):
        if not root: return 'x'
        return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data):
        # The reason I use self.data in the deserialize is, data stream will be consumed  as we build left side of Tree
        # by the time when the right side is building up, we need to hold what is left over.
        # Therefore, self.data is a global value, right side will use what is left over after tree is partially built
        self.data = data
        if self.data[0] == 'x': return None
        node = TreeNode(self.data[:self.data.find(',')])
        node.left = self.deserialize(self.data[self.data.find(',') + 1:])
        node.right = self.deserialize(self.data[self.data.find(',') + 1:])
        return node


# Your Codec object will be instantiated and called as such:
t = TreeNode(3)
#t.left = TreeNode(4)
t.right = TreeNode(7)
#t.left.left = TreeNode(9)
#t.left.right = TreeNode(10)
ser = Codec()
deser = Codec()
print(ser.serialize(t))
ans = ser.serialize(deser.deserialize(ser.serialize(t)))
print(ans)