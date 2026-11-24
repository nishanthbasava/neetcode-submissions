class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom-Up Solution:
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for n in range(1, amount + 1):
            for coin in coins:
                if coin <= n:
                    dp[n] = min(dp[n], dp[n - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

        '''
        Top-Down Solution:
        memo = {0:0}

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
        '''