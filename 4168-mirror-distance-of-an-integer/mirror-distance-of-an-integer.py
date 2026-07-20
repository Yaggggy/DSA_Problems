class Solution:
    def mirrorDistance(self, n: int) -> int:
        s = str(n)
        return abs(n - int(s[-1::-1]))