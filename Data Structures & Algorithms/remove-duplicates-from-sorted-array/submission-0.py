class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Time Complexity: O(n)
        #Space Complexity: O(1)

        read = 0 
        write = 0

        seen = set()

        while read < len(nums):
            if nums[read] in seen:
                read += 1
            else:
                nums[write] = nums[read]
                seen.add(nums[read])
                read += 1
                write += 1
        
        return write