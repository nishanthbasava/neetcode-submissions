class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        i = 0
        #red
        if 0 in freq:
            for j in range(freq[0]):
                nums[i] = 0
                i += 1
        
        #white
        if 1 in freq:
            for j in range(freq[1]):
                nums[i] = 1
                i += 1
            
        #blue
        if 2 in freq:
            for j in range(freq[2]):
                nums[i] = 2
                i += 1