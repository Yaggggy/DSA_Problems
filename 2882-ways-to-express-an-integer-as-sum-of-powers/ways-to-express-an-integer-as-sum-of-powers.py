class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = int(1e9) + 7
        powers = []
        for i in range(1, n+1):
            if i**x > n:
                break
            powers.append(i**x)

        dp = [0] * (n+1)
        dp[0] = 1

        for p in powers:
            for j in range(n, p-1, -1):
                dp[j] = (dp[j] + dp[j-p]) % mod
        return dp[n]