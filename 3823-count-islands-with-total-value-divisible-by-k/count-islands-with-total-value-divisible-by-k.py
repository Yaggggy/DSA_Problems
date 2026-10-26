class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                
                queue = deque([(i, j)])
                curr = grid[i][j]
                grid[i][j] = 0
                while queue:
                    pi, pj = queue.popleft()

                    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        ni = pi + di
                        nj = pj + dj

                        if not (0 <= ni < m and 0 <= nj < n):
                            continue
                        if grid[ni][nj] == 0:
                            continue

                        curr += grid[ni][nj]
                        grid[ni][nj] = 0
                        queue.append((ni, nj))
                
                if curr % k == 0:
                    count += 1

        return count