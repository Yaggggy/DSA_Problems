class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        i, j, n=nums.index(min(nums)), nums.index(max(nums)), len(nums)
        if i>j: i, j=j, i
        return min(i+1+n-j, j+1, n-i)