from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0 
        fin = 0 
        for i in counter :
            
            if counter[i] > ans :
                ans = counter[i]
                fin = ans
            elif counter[i] == ans :
                fin += counter[i]
            else:
                continue 
        return fin
        