class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ans = []
        nums.sort()
        for i , value in enumerate(nums):
            if value == target :
                ans.append(i)
        return ans 