class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        fib = []
        for i in range(n+1):
            if len(fib) <= 1:
                fib.append(1)
            else:
                fib.append(fib[i-1]+fib[i-2])
        return fib[-1]