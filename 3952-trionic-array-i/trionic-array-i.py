class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums) 
    
        def inc(st):
            for i in range(st,n-1):
                if nums[i] < nums[i+1]:
                    continue 
                else:
                    return i 
            return n-1 
    
        def dec(st):
            for i in range(st,n-1):
                if nums[i] > nums[i+1]:
                    continue 
                else:
                    return i 
            return n-1 

        p = inc(0)
        if p == 0 or p == n-1 :
            return False 
        
        q = dec(p)
        if q == p or q == n - 1 :
            return False 
        
        r = inc(q)
        if r != n-1 :
            return False 
        
        return True 