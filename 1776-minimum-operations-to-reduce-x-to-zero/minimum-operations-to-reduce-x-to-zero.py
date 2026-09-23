class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        n = len(nums)
        left = 0
        cur = 0
        best = -1

        for right in range(n):
            cur += nums[right]
            while cur > target and left <= right:
                cur -= nums[left]
                left += 1
            if cur == target:
                best = max(best, right - left + 1)

        return n - best if best != -1 else -1