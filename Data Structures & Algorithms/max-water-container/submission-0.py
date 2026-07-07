class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        p1 = 0
        p2 = len(heights) - 1
        maxArea = 0
        area = 0

        while p1 < p2:
            
            if heights[p1] < heights[p2]:
                area = heights[p1] * (p2 - p1)
            else:
                area = heights[p2] * (p2 - p1)
                
            maxArea = max(area, maxArea)

            if heights[p1] < heights[p2]:
                p1 += 1
            elif heights[p1] > heights[p2]:
                p2 -= 1
            else: #same height
                if heights[p1 + 1] < heights[p2 - 1]:
                    p2 -= 1
                else:
                    p1 += 1

        return maxArea