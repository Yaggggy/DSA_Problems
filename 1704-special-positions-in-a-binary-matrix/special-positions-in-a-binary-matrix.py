class Solution:
    def numSpecial(self, mat):
        m = len(mat)
        n = len(mat[0])

        rowSum = [sum(row) for row in mat]
        colSum = [sum(mat[i][j] for i in range(m)) for j in range(n)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rowSum[i] == 1 and colSum[j] == 1:
                    ans += 1

        return ans