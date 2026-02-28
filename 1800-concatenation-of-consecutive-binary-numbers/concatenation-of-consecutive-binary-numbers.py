class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10 ** 9 + 7
        val = 1

        next_shift = 2
        shifter = 2

        for i in range(2, n+1):
            if i >= next_shift:
                next_shift *= 2
                shifter = (shifter * 2) % mod

            val = ((val * shifter) + i) % mod
        
        return val