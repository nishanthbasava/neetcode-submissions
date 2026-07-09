class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(logn)
        # Space Complexity: O(1)

        p1 = 0 
        p2 = len(nums) - 1

        while p1 <= p2:
            p3 = (p1 + p2) // 2

            if nums[p3] < target:
                p1 = p3 + 1
            elif nums[p3] > target:
                p2 = p3 - 1
            else:
                return p3

        return -1