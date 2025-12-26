class Solution:
    def bestClosingTime(self, customers: str) -> int:
        c = customers
        length = len(c)
        result = 0
        resultIdx = -1
        accum = 0
        for i in range(length):
            if c[i] == "Y":
                accum += 1
            else:
                accum -= 1
            
            if accum > result:
                result = accum
                resultIdx = i
        
        return resultIdx + 1