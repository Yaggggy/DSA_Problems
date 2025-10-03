class MyStack:

    def __init__(self):
        self.stk1 = []
        self.stk2 = [] 

    def push(self, x: int) -> None:
        while self.stk1:
            self.stk2.append(self.stk1.pop())
        self.stk1.append(x)
        while self.stk2 :
            self.stk1.append(self.stk2.pop()) 

    def pop(self) -> int:
        val = self.stk1[0]
        self.stk1 = self.stk1[1:]
        return val

    def top(self) -> int:
        return self.stk1[0]

    def empty(self) -> bool:
            return len(self.stk1) == 0
        