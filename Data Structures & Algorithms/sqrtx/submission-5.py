class Solution:
    def mySqrt(self, x: int) -> int:
        # Time Complexity: O(logn)
        # Space Complexity: O(1)

        p1 = 0
        p2 = x 

        while p1 <= p2:
            mid = (p1 + p2) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                p1 = mid + 1

            else: 
                p2 = mid - 1

        return p2