class Solution:
    def mySqrt(self, x: int) -> int:
        # Time Complexity: O(logn)
        # Space Complexity: 

        p1 = 0
        p2 = x

        while p1 <= p2:
            p3 = (p1 + p2) // 2

            if p3 * p3 == x:
                return p3
            elif p3 * p3 < x:
                p1 = p3 + 1
            else: # p3 * p3 > x
                p2 = p3 - 1
            
        return p2