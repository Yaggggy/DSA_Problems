class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def ways(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            count = 0
            if s[i] == t[j]:
                count += ways(i+1, j+1)
            count += ways(i+1, j)
            return count
        return ways(0, 0)