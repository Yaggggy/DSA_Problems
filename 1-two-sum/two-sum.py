class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index , num in enumerate(nums):
            comp = target - num 
            if comp in hash :
                return [hash[comp],index]
            hash[num] = index 
                