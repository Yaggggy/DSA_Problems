class Solution:
    def minMoves(self, nums):
        mn = min(nums)
        return sum(nums) - len(nums) * mn