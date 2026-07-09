class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        p1 = 0 
        p2 = len(nums)

        while p1 < p2:
            mid = (p1 + p2) // 2

            if nums[mid] >= target:
                if nums[mid] == target:
                    return mid

                p2 = mid
            
            else: 
                p1 = mid + 1

        return p2