class MyStack:

    def __init__(self):
        self.main_q = []
        self.helper_q = [] 

    def push(self, x: int) -> None:
        self.helper_q.append(x)
        self.helper_q.extend(self.main_q)
        self.main_q.clear()

        self.helper_q , self.main_q = self.main_q , self.helper_q


    def pop(self) -> int:
        val = self.main_q[0]
        self.main_q = self.main_q[1:]
        return val

    def top(self) -> int:
        return self.main_q[0]

    def empty(self) -> bool:
            return len(self.main_q) == 0
        