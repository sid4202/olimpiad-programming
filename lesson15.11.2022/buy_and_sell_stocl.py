class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = prices[1] - prices[0]
        minimum_in_slice = prices[0]
        for i in range(1, len(prices)):
            minimum_in_slice = min(minimum_in_slice, prices[i])

            max_profit = max(prices[i] - minimum_in_slice, max_profit)

        return max(0, max_profit)

