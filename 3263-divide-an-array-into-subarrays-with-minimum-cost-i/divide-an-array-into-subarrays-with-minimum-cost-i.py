class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]

        nums.pop(0)
        nums.sort()
        return ans + nums[0] + nums[1]