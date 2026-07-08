class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(logn)
        # Space Complexity: O(1)

        p1 = 0
        p2 = len(nums) - 1

        while p2 >= p1:
            p3 = (p1 + p2) // 2
            if nums[p3] == target:
                return p3
            elif nums[p3] > target:
                p2 = p3 - 1
            else: #nums[p3] < target
                p1 = p3 + 1

        return -1