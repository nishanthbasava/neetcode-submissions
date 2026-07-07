class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        i = 0
        for j in range(3):
            for k in range(freq.get(j, 0)):
                nums[i] = j
                i += 1