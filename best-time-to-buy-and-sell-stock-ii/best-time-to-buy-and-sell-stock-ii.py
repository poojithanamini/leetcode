class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last, result = prices[0], 0
        
        for i in prices:
            if i > last:
                result += i - last
            last = i
        
        return result