class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Bottom-Up Approach

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        prev1, prev2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            prev1, prev2 = prev2, max(prev1 + nums[i], prev2)
        
        return prev2
        
        
        
        '''
        # Top-Down Approach

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
        
