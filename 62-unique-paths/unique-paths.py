class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m
        row = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                row[j] = row[j] + row[j - 1]
        return row[n - 1]