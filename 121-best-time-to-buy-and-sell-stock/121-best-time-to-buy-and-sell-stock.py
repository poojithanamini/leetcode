class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        buyPrice = prices[0]
        maxProfit = 0
        
        i = 1
        while i < len(prices):
            profit = prices[i] - buyPrice
            
            # maximize sell value
            maxProfit = max(maxProfit, profit)
            
            # minimize buy value
            buyPrice = min(buyPrice, prices[i])
            
            i += 1
            
        return maxProfit