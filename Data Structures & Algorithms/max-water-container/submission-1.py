class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        p1 = 0
        p2 = len(heights) - 1
        maxArea = 0
        area = 0

        while p1 < p2:
            area = min(heights[p1], heights[p2]) * (p2 - p1)
            maxArea = max(area, maxArea)

            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1

        return maxArea