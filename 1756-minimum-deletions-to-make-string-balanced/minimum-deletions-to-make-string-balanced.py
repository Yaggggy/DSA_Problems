class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = 0 
        b = 0 
        for i in s :
            if i == 'b':
                b += 1 
            else :
                ans = min(ans + 1 , b)
        return ans