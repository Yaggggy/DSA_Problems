class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []

        for i in operations :
            if i == "+":
                stk.append(stk[-1]+ stk[-2])
            elif i == "D" :
                stk.append(stk[-1]*2)
            elif i == "C":
                stk.pop()
            else:
                stk.append(int(i))
        
        return sum(stk)