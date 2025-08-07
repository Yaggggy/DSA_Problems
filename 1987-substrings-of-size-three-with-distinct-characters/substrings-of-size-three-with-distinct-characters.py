class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        i = 0 
        j = 3 
        count = 0
        if len(s) < 3 :
            return count
        while j <= n :
            check = len(set(s[i:j]))
            i += 1 
            j += 1 
            if check == 3 :
                count += 1 
            else:
                continue
        return count