class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        slow = 0
        fast = 0

        while True:
            if slow == fast:
                fast = fast + 1 if fast + 1 < len(nums) else 0

            if nums[slow] == nums[fast]:
                return nums[slow]

            slow = slow + 1 if slow + 1 < len(nums) else 0
            fast = fast + 1 if fast + 1 < len(nums) else 0
            fast = fast + 1 if fast + 1 < len(nums) else 0