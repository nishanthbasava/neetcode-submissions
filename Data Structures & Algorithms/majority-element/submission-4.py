class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boyer-Moore's algorithm
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if candidate == num:
                count += 1
            else: #different element
                count -= 1

        return candidate                