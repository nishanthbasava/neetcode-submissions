class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        
        for num in nums:
            if num not in freq:
                freq[num] = 1

            else:
                freq[num] += 1

        max = 0
        max_num = nums[0] 
        for num in freq:
            if freq[num] > max:
                max = freq[num]
                max_num = num

        return max_num