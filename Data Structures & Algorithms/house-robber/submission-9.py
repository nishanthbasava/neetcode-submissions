class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {} #index i -> max till that index

        def dfs(i):
            if i in memo: 
                return memo[i]

            if i < 0:
                return 0

            memo[i] = max(dfs(i-2) + nums[i], dfs(i-1))
            return memo[i]

        return dfs(len(nums) - 1)