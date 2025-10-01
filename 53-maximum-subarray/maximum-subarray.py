class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('-inf')
        curr = 0 
        for i in range(n):
            curr += nums[i]
            ans = max(ans,curr)
            curr = max(curr,0)
        return ans