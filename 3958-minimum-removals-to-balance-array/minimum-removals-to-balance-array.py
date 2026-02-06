class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        left = 0
        best = 0
        
        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1
            
            best = max(best, right - left + 1)
        
        return n - best