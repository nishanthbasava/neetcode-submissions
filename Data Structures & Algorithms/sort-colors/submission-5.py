class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # One pass, Dutch National Flag algorithm

        p0 = 0 
        px = 0
        p2 = len(nums) - 1

        while px <= p2:
            if nums[px] == 0:
                nums[px] = nums[p0]
                nums[p0] = 0
                p0 += 1
                px += 1
            elif nums[px] == 2:
                nums[px] = nums[p2]
                nums[p2] = 2
                p2 -= 1
            else:
                px += 1
            
            