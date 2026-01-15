class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        m = len(s)
        n = len(t)
        check = 0 
        i = j = 0 
        
        while i < n and j < m :
            if s[j] == t[i]:
                i += 1 
                j += 1 
                check += 1 
            else :
                i += 1 
        
        return check == m 
                
