class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(start, cur, subset):
            if cur > target:
                return
            if cur == target:
                output.append(subset.copy())
                return
            for j in range(start, len(nums)):
                subset.append(nums[j])
                dfs(j, cur + nums[j], subset)   # j, not j + 1: reuse allowed
                subset.pop()

        dfs(0, 0, [])
        return output