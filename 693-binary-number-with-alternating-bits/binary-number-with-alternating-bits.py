class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)
        for i in range(2,len(s)-1):
            if s[i] == s[i+1]:
                return False
        return True 