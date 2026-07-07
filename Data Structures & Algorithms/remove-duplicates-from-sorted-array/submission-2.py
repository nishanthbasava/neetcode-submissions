class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Time Complexity: O(n)
        #Space Complexity: O(1)

        write = 0

        for read in range(len(nums)):
            if nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]

        return write + 1