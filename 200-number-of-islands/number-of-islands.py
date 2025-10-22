class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])

        visited = [[False for _ in range(N)] for _ in range(M)]
        def dfs(idx, jdx):

            if grid[idx][jdx] == "0" or visited[idx][jdx]:
                return False
            
            visited[idx][jdx] = True

         
            for adjX, adjY in [(idx-1, jdx), (idx+1, jdx), (idx, jdx-1), (idx, jdx+1)]:
                if adjX < 0 or adjX >= M or adjY < 0 or adjY >= N:
                    continue
                if visited[adjX][adjY]:
                    continue
                dfs(adjX, adjY)
            
            return True

        ans = 0
        for idx in range(M):
            for jdx in range(N):
                isNewIsland = dfs(idx, jdx)
                if isNewIsland:
                    ans += 1

        return ans