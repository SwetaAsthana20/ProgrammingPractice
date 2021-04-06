class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = 0
        self.temp = []

    def push(self, x: int) -> None:
        if not self.temp:
            self.min = x
            self.temp.append(x)

        elif x < self.min:
            self.temp.append((2 * x) - self.min)
            self.min = x

        else:
            self.temp.append(x)

    def pop(self) -> None:
        z = self.temp.pop()
        if z < self.min:
            self.min = ((2 * self.min) - z)

    def top(self) -> int:
        z = self.temp[-1]
        if z < self.min:
            return self.min
        return z

    def getMin(self) -> int:
        return self.min


obj = MinStack()
obj.push(7)
obj.pop()
obj.push(-1)
print(obj.getMin())
obj.push(0)
print(obj.getMin())
obj.push(-9)
obj.push(3)
print(obj.top())
print(obj.getMin())