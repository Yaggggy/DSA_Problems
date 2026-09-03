class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        
        if min_val % 2 != 0:
            return True
            
        for num in nums1:
            if num % 2 != 0:
                return False
                
        return True