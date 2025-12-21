class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        
        par = 1 
        n = len(nums)
        ans = 0
        while par != n:
            l = nums[:par]
            r = nums[par:]
            if abs(sum(l) - sum(r)) % 2 == 0 :
                ans += 1 
            par += 1 
        return ans