class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        nums.sort()
        ans = []
        
        count = nums.count(target) 
        if count < 1 :
            return ans 
        else:
            
            index = nums.index(target)
            for i in range(count):
                ans.append(index)
                index += 1 
        
        return ans
            