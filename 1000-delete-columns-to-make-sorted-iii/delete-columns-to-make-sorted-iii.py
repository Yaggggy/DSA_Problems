class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs[0])
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                ok = True
                for row in strs:
                    if row[j] > row[i]:
                        ok = False
                        break
                if ok:
                    dp[i] = max(dp[i], dp[j] + 1)
        return n - max(dp)