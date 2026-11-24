class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(n):
            if n == 1 or n == 2:
                return n

            if n in memo:
                return memo[n]

            memo[n] = dfs(n-2)  + dfs(n-1)

            return memo[n]

        return dfs(n)