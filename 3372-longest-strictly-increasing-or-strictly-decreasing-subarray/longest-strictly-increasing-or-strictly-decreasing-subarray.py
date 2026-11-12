class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        incr, decr, ans = 1,1,1
        prev = nums.pop(0)

        for num in nums:

            incr = incr * (num > prev) + 1
            decr = decr * (num < prev) + 1
            prev = num

            ans = max(ans, incr, decr)
            
        return ans