class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0 
        buy = float("inf")

        for i in prices : 
            if i < buy :
                buy = i 
            
            profit = max(profit , i - buy)

        return profit 