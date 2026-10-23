class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Time Complexity: O(nlogm)
        #Space Complexity: O(1)

        lo = 1
        hi = max(piles)

        def cond(i):
            hours = 0
            for pile in piles:
                hours += (pile + i - 1) // i

            return hours <= h

        while lo < hi:
            mid = (lo + hi) // 2

            if cond(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo