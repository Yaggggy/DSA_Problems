class Solution:
    def isValid(self, s: str) -> bool:
        map = {')':'(',']':'[','}':'{'}
        stk = []
        for i in s :
            if i in map.values():
                stk.append(i)
            elif i in map :
                if not stk or map[i] != stk.pop():
                    return False 
        return not stk 