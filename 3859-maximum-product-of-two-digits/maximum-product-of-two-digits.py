class Solution:
    def maxProduct(self, n: int) -> int:
        a = str(n)
        s = [x for x in a]
        s.sort()
        return int(s[-1]) * int(s[-2])
        