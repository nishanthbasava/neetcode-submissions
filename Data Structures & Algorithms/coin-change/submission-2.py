class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0} # amnt -> min number of coins to get to that amount

        def dfs(i):
            if i in memo:
                return memo[i]

            if i < 0:
                return float('inf')

            cur = float('inf')
            for coin in coins:
                cur = min(cur, dfs(i-coin) + 1)

            memo[i] = cur

            return memo[i]

        answer = dfs(amount)
        return answer if answer != float('inf') else -1