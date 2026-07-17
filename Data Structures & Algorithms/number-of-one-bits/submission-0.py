class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time Complexity: O(1)
        # Space Complexity: O(1)

        count = 0

        for i in range(32):
            count += n & 1
            n >>= 1

        return count