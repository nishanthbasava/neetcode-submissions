class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(n):
            if n < 0:
                return 0
            
            if n == 0:
                return 1

            if n in memo:
                return memo[n]

            x = dfs(n-2)
            memo[n-2] = x

            return x + dfs(n-1)

        return dfs(n)