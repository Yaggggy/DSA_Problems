class Solution:
    def createGrid(self, m, n):
        top = "." * n
        rest = "#" * (n - 1) + "."
        return [top] + [rest] * (m - 1)