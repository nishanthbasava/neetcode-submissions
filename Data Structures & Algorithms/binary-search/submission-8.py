class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(logn)
        # Space Complexity: O(1)

        from bisect import bisect_left

        i = bisect_left(nums, target)

        return i if (i <= len(nums) - 1) and nums[i] == target else -1