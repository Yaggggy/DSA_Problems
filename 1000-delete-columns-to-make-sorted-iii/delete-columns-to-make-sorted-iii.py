from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        dp = [1] * m  
        
        for j in range(m):
            for i in range(j):
                valid = True
                for r in range(n):
                    if strs[r][i] > strs[r][j]:
                        valid = False
                        break
                if valid:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return m - max(dp)