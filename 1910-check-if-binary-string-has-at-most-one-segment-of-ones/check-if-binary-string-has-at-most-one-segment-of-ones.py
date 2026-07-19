class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        if len(s)<3:
            return True

        for i in range(1,len(s)):
            if s[i]=="0" and "1" in s[i:]:
                return False
        return True