class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        ans = -1
        for key,value in counter.items() :
            if key == value :
                ans = max(ans,key) 
        
        return ans