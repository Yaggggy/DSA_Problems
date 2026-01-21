class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 1
        def isMagic(r, c, k):
            target = sum(grid[r][c:c+k])
            # rows
            for i in range(r, r+k):
                if sum(grid[i][c:c+k]) != target:
                    return False
            # columns
            for j in range(c, c+k):
                if sum(grid[i][j] for i in range(r, r+k)) != target:
                    return False
            # diagonals
            if sum(grid[r+i][c+i] for i in range(k)) != target:
                return False
            if sum(grid[r+i][c+k-1-i] for i in range(k)) != target:
                return False
            return True
        for r in range(m):
            for c in range(n):
                for k in range(2, min(m-r, n-c)+1):
                    if isMagic(r, c, k):
                        ans = max(ans, k)
        return ans