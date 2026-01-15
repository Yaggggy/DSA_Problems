class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        ans = 0 
        for i in prices :
            if i < low :
                low = i 
            
            profit = i - low 
            if profit > ans :
                ans = profit 
        return ans