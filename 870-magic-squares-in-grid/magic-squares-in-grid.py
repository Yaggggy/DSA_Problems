class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def valid(row, column):
            if grid[row+1][column+1]!=5:
                return 0 
            seen = set()
            c = [0] * 3
            r = [0] * 3
            for i in range(3):
                for j in range(3):
                    number = grid[row + i][column + j]
                    if number > 9 or number < 1 or number in seen:
                        return 0
                    seen.add(number)
                    c[j] += number
                    r[i] += number
            rowSum = r[0] == r[1] == r[2]
            colSum = c[0] == c[1] == c[2]
            diagonalSum = grid[row][column] + grid[row + 2][column + 2] == grid[row][column + 2] + grid[row + 2][column]
            return 1 if diagonalSum and rowSum and colSum else 0

        rows, columns = len(grid), len(grid[0])
        count = 0

        for row in range(rows - 2):
            for column in range(columns - 2):
                count += valid(row, column)
        return count