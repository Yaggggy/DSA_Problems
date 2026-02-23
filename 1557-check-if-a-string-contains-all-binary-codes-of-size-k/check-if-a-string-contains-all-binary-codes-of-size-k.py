class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        d={}
        if k>len(s):
            return False
        i,j=0,k-1
        while j<len(s):
            d[int(s[i:j+1],2)]=1
            i+=1
            j+=1
        for i in range(1<<k):
            if i not in d: 
                return False
        return True