class Node:
    def __init__(self, n, v, m):
        self.neighbor = n
        self.val = v
        self.min = m

class MinStack:

    def __init__(self):
        self.tail = None

    def push(self, val: int) -> None:
        if not self.tail:
            minimum = val
        else:
            minimum = min(val, self.tail.min)
        new = Node(self.tail, val, minimum)
        self.tail = new

    def pop(self) -> None:
        self.tail = self.tail.neighbor

    def top(self) -> int:
        return self.tail.val

    def getMin(self) -> int:
        return self.tail.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()