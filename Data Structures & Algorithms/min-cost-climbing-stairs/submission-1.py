class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Now let's try the bottom-down approach, which would ideally have the same recurrence but only O(1) space
        # Each problem only requires the answers to the two previous problems

        prev2, prev1 = 0, 0

        for i in range(2, len(cost) + 1):
            prev1, prev2 = prev2, min(prev1 + cost[i-2], prev2 + cost[i-1])
        
        return prev2

        
        '''
        This is the top-down approach, which requires memoization and O(n) space

        memo = {0: 0, 1: 0} # i => min cost to get to that step

        def dfs(i):
            if i in memo:
                return memo[i]

            memo[i] = min(dfs(i-1) + cost[i-1], dfs(i-2) + cost[i-2])
            return memo[i]

        return dfs(len(cost)) 
        '''