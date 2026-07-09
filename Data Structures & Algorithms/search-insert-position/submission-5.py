class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        p1 = 0 
        p2 = len(nums) - 1

        while p1 <= p2:
            p3 = (p1 + p2) // 2

            if nums[p3] < target:
                p1 = p3 + 1
            elif nums[p3] > target:
                p2 = p3 - 1
            else:
                return p3

        return p1