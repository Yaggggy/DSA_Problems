class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = 0 
        second = 0 

        for i in nums :
            if i > first :
                second = first 
                first = i  
            elif i > second :
                second = i 

        return (first-1) * (second-1)