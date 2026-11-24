class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        def dfs(i, cur):
            nonlocal total
            if i == len(nums):
                total += cur

            else:
                dfs(i + 1, cur ^ nums[i])
                dfs(i + 1, cur)
            
        dfs(0, 0)
        return total