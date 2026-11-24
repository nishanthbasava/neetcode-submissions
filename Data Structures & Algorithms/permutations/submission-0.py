class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(subset):
            if len(subset) == len(nums):
                output.append(subset.copy())
                return

            for num in nums:
                if num not in subset:
                    subset.append(num)
                    dfs(subset)
                    subset.pop()

        dfs([])
        return output
            
                