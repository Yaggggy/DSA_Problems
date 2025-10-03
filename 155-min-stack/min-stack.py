class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []
    def push(self, val: int) -> None:
        self.stk.append(val)
    def pop(self) -> None:
        if self.stk :
            self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return min(self.stk)        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()