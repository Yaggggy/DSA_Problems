class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n 
        right = [0] * n 

        if n == 1 :
            return [0] 
        
        for i in range(1,n):
            left[i] = sum(nums[:i])
            right[i-1] = sum(nums[i:])
        
        ans = []
        for i in range(n):
            ans.append(abs(left[i]-right[i]))
        return ans