class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre_max = [0] * n
        pre_max[0] = nums[0]
        cur = nums[0]

        for i in range(1, n):
            cur = max(nums[i], cur)
            pre_max[i] = cur
        

        suf_min = nums[-1]
        for i in range(n - 2, -1, -1):
            if pre_max[i] > suf_min:
                pre_max[i] = pre_max[i + 1]
            suf_min = min(suf_min, nums[i])
        return pre_max