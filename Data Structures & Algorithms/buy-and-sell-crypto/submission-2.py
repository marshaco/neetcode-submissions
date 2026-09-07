class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        i, j = 0, 1
        while j < len(prices):
            nProfit = prices[j] - prices[i]
            if nProfit > profit:
                profit = nProfit

            if prices[j] <= prices[i]:
                i = j
                j += 1
            else:
                j += 1
        return profit