class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        maxProfit = 0
        l = 0

        for r in range(len(prices)):
            price = prices[r]
            
            if price < buy:
                buy = price
            else:
                maxProfit = max(maxProfit, price-buy)
        return maxProfit
