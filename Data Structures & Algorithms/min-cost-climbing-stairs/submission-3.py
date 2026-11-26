class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Bottom-Up 
        # First, build the recurrence and see what exactly that each dfs depends on

        older, newer = 0, 0
        for i in range(2, len(cost) + 1):
            older, newer = newer, min(older + cost[i-2], newer + cost[i-1])

        return newer
        
        '''
        Top-Down 1D DP
        memo = {0:0, 1:0}

        def dfs(i):
            if i in memo:
                return memo[i]

            memo[i] = min(dfs(i-1) + cost[i-1], dfs(i-2) + cost[i-2])
            return memo[i]

        return dfs(len(cost))
        '''