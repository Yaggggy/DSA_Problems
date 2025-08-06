class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')
        for i in nums :
            r = 0 
            while i > 0 :
                r += i % 10 
                i //= 10 
            ans = min(ans,r)
        return ans
        