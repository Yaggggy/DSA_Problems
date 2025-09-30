class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        s = set(nums)

        for i in range(n+1):
            if i not in s :
                return i 
        