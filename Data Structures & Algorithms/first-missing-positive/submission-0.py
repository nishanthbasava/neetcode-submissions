class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)

        for i in range(1, 100000):
            if i not in seen:
                return i