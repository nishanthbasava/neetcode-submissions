class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        stk = []
        areas = [0] * len(heights)
        width = 0

        #forward pass
        for i, height in enumerate(heights):
            while stk and stk[-1][1] > height:
                popped = stk.pop()
                width = i - popped[0]
                areas[popped[0]] += popped[1] * width
                width += 1

            stk.append((i, height))

        #remaining
        while stk:
            popped = stk.pop()
            width = len(heights) - popped[0]
            areas[popped[0]] += popped[1] * width

        # stk = []
        #backward pass
        heights.reverse()
        for i, height in enumerate(heights):
            while stk and stk[-1][1] > height:
                popped = stk.pop()
                width = i - popped[0]
                areas[len(heights) - 1 - popped[0]] += popped[1] * (width - 1)

            stk.append((i, height))

        #remaining
        while stk:
            popped = stk.pop()
            width = len(heights) - popped[0] - 1
            areas[len(heights) - 1 - popped[0]] += popped[1] * width

        return max(areas)