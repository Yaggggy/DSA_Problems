class Solution:
    def maxOperations(self, s: str) -> int:
        out = 0
        oneCount = 0
        firstZero = True
        
        for char in s:
            if char == "1":
                oneCount += 1
                firstZero = True

            elif firstZero == True:
                firstZero = False
                out += oneCount
        
        return out