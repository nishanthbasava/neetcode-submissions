class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Bottom-Up Approach
        older, newer = 0, 0

        for x in nums:
            older, newer = newer, max(newer, older + x)

        return newer
        
        
        
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
        
