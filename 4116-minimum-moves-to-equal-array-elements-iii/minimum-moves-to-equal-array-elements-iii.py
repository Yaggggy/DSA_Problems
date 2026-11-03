class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        ans = 0
        
        for i in nums:
            ans += mx - i

        return ans