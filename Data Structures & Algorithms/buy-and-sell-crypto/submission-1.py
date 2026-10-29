class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1

        max_prof = 0

        while sell < len(prices):

            if (prices[buy] >= prices[sell]):
                buy = sell
            
            else:
                profit = prices[sell] - prices[buy]
                max_prof = max(profit, max_prof)

            sell += 1

        return max_prof