class Solution:
    def rob(self, nums: List[int]) -> int:
        # Top Down Approach

        if len(nums) == 1: 
            return nums[0]

        memo = {0:nums[0], 1:max(nums[0], nums[1])}

        def dfs(i):
            if i in memo: 
                return memo[i]

            memo[i] = max(dfs(i - 1), dfs(i - 2) + nums[i])

            return memo[i]

        return dfs(len(nums) - 1)

        '''
        Bottom-Up Approach

        if len(nums) == 1:
            return nums[0]

        prev1, prev2 = nums[0], nums[1]

        for i in range(2, len(nums)):
            prev1, prev2 = 

            '''