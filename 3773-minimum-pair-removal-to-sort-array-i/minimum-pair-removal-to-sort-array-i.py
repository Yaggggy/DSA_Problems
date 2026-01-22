class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if len(nums) == 1:  
            return 0
        
        count = 0
        while not self.sorted(nums):
            minSum = float('inf')

            fst = 0
            snd = 1 
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < minSum:
                    minSum = nums[i] + nums[i + 1]
                    fst = i 
                    snd = i + 1
            nums.pop(snd)   
            nums.pop(fst)            
            nums.insert(fst,minSum)
            count += 1
        return count
        
    def sorted(self, arr):
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                return False
        return True
    
        

         
