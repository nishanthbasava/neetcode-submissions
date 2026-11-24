class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {coin:1 for coin in coins}
        memo[0] = 0

        def dfs(n):
            if n in memo:
                return memo[n]

            if n < 0:
                return float('inf')

            cur_min = float('inf')
            for coin in coins:
                cur_min = min(cur_min, dfs(n-coin) + 1)

            memo[n] = cur_min
            return cur_min

        output = dfs(amount)
        if output == float('inf'):
            return -1
        return output