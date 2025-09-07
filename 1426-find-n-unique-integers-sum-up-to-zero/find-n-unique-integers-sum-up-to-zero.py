class Solution:
    def sumZero(self, n: int) -> list[int]:
        out = [0] * n
        left, right = 0, n - 1
        num = 1
        while left < right:
            out[left] = num
            out[right] = -num
            num += 1
            left += 1
            right -= 1
        return out