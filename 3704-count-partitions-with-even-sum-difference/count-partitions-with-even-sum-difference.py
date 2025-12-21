class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        curr,count = 0,0
        for i in range(len(nums)-1):
            num = nums[i]
            curr+=num
            right = total-curr
            if abs(curr-right)%2==0:
                count+=1
        return count