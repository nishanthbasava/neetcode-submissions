class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {} # i -> number of ways to solve the rest

        def dfs(i):
            if i in memo:
                return memo[i]

            if i > len(s) - 1:
                return 1

            if s[i] == "0":
                memo[i] = 0
            
            elif s[i] == "1" and i+1 <= len(s) - 1:
                memo[i] = dfs(i+1) + dfs(i+2)

            elif s[i] == "2" and i+1 <= len(s) - 1 and s[i+1] in "0123456":
                memo[i] = dfs(i+1) + dfs(i+2)
            
            else:
                memo[i] = dfs(i+1)
            
            return memo[i]

        return dfs(0)