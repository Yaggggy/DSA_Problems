class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        result = 0
        cols = len(matrix[0])
        dp = [0] * cols

        for row in matrix:
            for i in range(cols):
                if row[i] == "1":
                    dp[i]+=1
                else:
                    dp[i] = 0   
            stack = []
            for j in range(cols+1):
                cur_val = dp[j] if j < cols else 0
                while stack and dp[stack[-1]] > cur_val:
                    height = dp[stack.pop()]
                    weidth = j if not stack else j-stack[-1]-1
                    result = max(result,height*weidth)
                stack.append(j)
        return result