class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(i, subset):
            nonlocal output

            if i == len(nums):
                output.append(subset.copy())

            else:
                dfs(i + 1, subset)
                subset.append(nums[i])
                dfs(i + 1, subset)
                subset.pop()

        dfs(0, [])
        return output