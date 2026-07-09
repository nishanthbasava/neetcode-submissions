class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(logn)
        # Space Complexity: O(1)

        p1 = 0
        p2 = len(nums) - 1

        while p1 < p2:
            mid = (p1 + p2) // 2

            if nums[mid] >= target:
                p2 = mid
            else: 
                p1 = mid + 1

        if p1 == len(nums) or nums[p1] != target:
            return -1

        return p1