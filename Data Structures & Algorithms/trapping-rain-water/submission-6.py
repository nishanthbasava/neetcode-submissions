class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)

        # left max
        cur = height[0]
        for i, h in enumerate(height):
            cur = max(cur, h)
            leftMax[i] = cur

        # right max
        cur = height[len(height) - 1]
        rightMax = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            cur = max(cur, height[i])
            rightMax[i] = cur

        #water
        water = 0
        for i in range(1, len(height) - 1):
            if height[i] < leftMax[i] and height[i] < rightMax[i]:
                water += min(leftMax[i], rightMax[i]) - height[i]
        
        return water