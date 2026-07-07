class Solution:
    def trap(self, height: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        left_max = [0] * len(height)
        right_max = [0] * len(height)
        amount = 0

        boundary = 0
        for i in range(1, len(height)): 
            boundary = max(boundary, height[i - 1])
            left_max[i] = boundary

        boundary = 0
        for i in range(len(height) - 2, -1, -1):
            boundary = max(boundary, height[i + 1])
            right_max[i] = boundary

        for i in range(len(height)):
            amount += max(0, min(left_max[i], right_max[i]) - height[i])

        return amount