class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        if len(nums_set) == 0:
            return 0

        length = 1
        count = 1
        min_num = min(nums_set)
        max_num = max(nums_set)

        i = min_num

        while i <= max_num:
            i += 1
            if i in nums_set:
                count += 1
            else:
                if count > length:
                    length = count
                count = 0

        return max(length, count)