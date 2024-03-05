class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for sell in prices[1:]:
            if buy < sell:
                profit = max(profit, sell-buy)
            else:
                buy = sell
        return profit


        