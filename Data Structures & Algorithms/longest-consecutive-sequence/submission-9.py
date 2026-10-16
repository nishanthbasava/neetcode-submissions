class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maximum = 0
        count = 0

        while num_set:
            starting = min(num_set)
            count = 1

            while starting + 1 in num_set:
                count += 1
                num_set.remove(starting)
                starting += 1
            
            num_set.remove(starting)
            maximum = max(count, maximum)

        return maximum

        # 2,3,4,5,10,20