class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 0 

        for i in range(n) :
            c = a + b
            a , b = c , a 
        return c 

