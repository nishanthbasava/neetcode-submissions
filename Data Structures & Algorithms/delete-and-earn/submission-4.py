class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Bottom-Up Approach
        from collections import Counter
        count = Counter(nums)
        
        older, newer = 0, 0

        for v in range(min(nums), max(nums) + 1):
            older, newer = newer, max(older + count[v] * v, newer)

        return newer

        
        '''
        Top-Down 1D Dynamic Programming Approach
        from collections import Counter

        count = Counter(nums)

        memo = {} # i => max up till that number (inclusive)

        def dfs(i):
            if i in memo:
                return memo[i]

            if i < 1:
                return 0
            
            if i not in count:
                return dfs(i-1)

            memo[i] = max(dfs(i-1), dfs(i-2) + count[i] * i)
            return memo[i]

        return dfs(max(nums))
        '''