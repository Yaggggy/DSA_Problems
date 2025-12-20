class Solution:
    def minDeletionSize(self, strs):
        r = len(strs)
        c = len(strs[0])
        ans = 0 

        for col in range(c):
            for ran in range(r-1):
                if strs[ran][col] > strs[ran+1][col]:
                    ans += 1
                    break 
        return ans