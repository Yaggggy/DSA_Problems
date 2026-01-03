class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
    
        for i in range(0, n-2, 3):
            if nums[i] == nums[i+1] or nums[i] == nums[i+2]:
                return nums[i]
            if nums[i+1] == nums[i+2]:
                return nums[i+1]

        return nums[n-1]