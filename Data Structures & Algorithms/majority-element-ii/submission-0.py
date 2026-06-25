class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_to_freq = {}

        for num in nums:
            if num not in num_to_freq:
                num_to_freq[num] = 1

            else:
                num_to_freq[num] += 1

        output = []

        for num in num_to_freq:
            if num_to_freq[num] > (len(nums) // 3):
                output.append(num)

        return output