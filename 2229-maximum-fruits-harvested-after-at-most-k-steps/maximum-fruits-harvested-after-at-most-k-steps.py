class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        n = len(fruits)
        maxFruits = 0
        left = 0
        total = 0
        
        for right in range(n):
            total += fruits[right][1]
            
            while left <= right:
                l_pos = fruits[left][0]
                r_pos = fruits[right][0]
                
                left_first = abs(startPos - l_pos) + (r_pos - l_pos)
                right_first = abs(startPos - r_pos) + (r_pos - l_pos)
                
                if min(left_first, right_first) <= k:
                    break 
                total -= fruits[left][1]
                left += 1
            
            maxFruits = max(maxFruits, total)
        
        return maxFruits