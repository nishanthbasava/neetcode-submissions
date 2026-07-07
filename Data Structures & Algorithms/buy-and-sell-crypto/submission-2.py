class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        min_buy_so_far = prices[0]
        profit = 0
        i = 1

        while i < len(prices):
            profit = max(profit, prices[i] - min_buy_so_far)
            min_buy_so_far = min(min_buy_so_far, prices[i])
            i += 1

        return profit