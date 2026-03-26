class Solution:
    def canPartitionGrid(self, grid):
        n = len(grid)
        col = len(grid[0])

        total = 0
        for i in range(n):
            for j in range(col):
                total += grid[i][j]

        from collections import Counter

        topFreq = Counter()
        bottomFreq = Counter()

        for i in range(n):
            for j in range(col):
                bottomFreq[grid[i][j]] += 1

        def check(val, r1, r2, c1, c2, mp):
            if val <= 0 or val not in mp:
                return False

            h = r2 - r1 + 1
            w = c2 - c1 + 1

            if h == 1 and w > 1:
                return grid[r1][c1] == val or grid[r1][c2] == val
            if w == 1 and h > 1:
                return grid[r1][c1] == val or grid[r2][c1] == val
            if h == 1 and w == 1:
                return grid[r1][c1] == val

            return True

        topSum = 0

        for i in range(n - 1):
            for j in range(col):
                v = grid[i][j]
                topSum += v
                topFreq[v] += 1
                bottomFreq[v] -= 1
                if bottomFreq[v] == 0:
                    del bottomFreq[v]

            bottomSum = total - topSum

            if topSum == bottomSum:
                return True

            removetop = 2 * topSum - total
            if check(removetop, 0, i, 0, col - 1, topFreq):
                return True

            removebot = total - 2 * topSum
            if check(removebot, i + 1, n - 1, 0, col - 1, bottomFreq):
                return True

        bottomFreq = Counter()
        for i in range(n):
            for j in range(col):
                bottomFreq[grid[i][j]] += 1

        leftFreq = Counter()
        leftSum = 0

        for j in range(col - 1):
            for i in range(n):
                v = grid[i][j]
                leftSum += v
                leftFreq[v] += 1
                bottomFreq[v] -= 1
                if bottomFreq[v] == 0:
                    del bottomFreq[v]

            rightSum = total - leftSum

            if leftSum == rightSum:
                return True

            removeleft = 2 * leftSum - total
            if check(removeleft, 0, n - 1, 0, j, leftFreq):
                return True

            removeright = total - 2 * leftSum
            if check(removeright, 0, n - 1, j + 1, col - 1, bottomFreq):
                return True

        return False