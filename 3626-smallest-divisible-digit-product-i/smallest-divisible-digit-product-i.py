class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:
            x = n
            prod = 1
            while x:
                prod *= x % 10
                x //= 10
            if prod % t == 0:
                return n

            n += 1