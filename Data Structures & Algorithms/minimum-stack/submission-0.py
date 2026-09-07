class MinStack:

    def __init__(self):
        self.s = []
        self.curMin = []

    def push(self, value: int) -> None:
        self.s.append(value)
        value = min(value, self.curMin[-1] if self.curMin else value)
        self.curMin.append(value)

    def pop(self) -> None:
        self.s.pop()
        self.curMin.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.curMin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()