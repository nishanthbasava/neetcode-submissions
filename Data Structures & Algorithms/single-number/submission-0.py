class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        ans = 0

        for num in nums:
            ans = ans ^ num

        return ans