class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        n = len(nums)
        res = float('inf')
        for i in range(n - k + 1):
            diff = nums[i + k - 1] - nums[i]
            res = min(res, diff)
        return res
