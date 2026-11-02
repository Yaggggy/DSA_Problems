class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        ans = 0 
        mid = nums[len(nums)// 2] 

        for i in nums :
            ans += abs(mid - i)
        
        return ans 
                

