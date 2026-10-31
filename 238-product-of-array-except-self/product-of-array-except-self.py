class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l_mult = 1 
        r_mult = 1 

        l_arr = [0] * n 
        r_arr = [0] * n 

        for i in range(n):
            j = -i-1 

            l_arr[i] = l_mult 
            l_mult *= nums[i]

            r_arr[j] = r_mult 
            r_mult *= nums[j] 
        
        return [x*y for x, y in zip(r_arr,l_arr)]