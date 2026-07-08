class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        p1 = 0 
        p2 = len(nums) - 1

        if target < nums[p1]:
            return 0
        
        if target > nums[p2]:
            return p2 + 1

        while p1 <= p2:
            p3 = (p1 + p2) // 2

            if p1 == p2 or p1 == p3 or p2 == p3:
                if target > nums[p1]:
                    return p1 + 1
                else:
                    return p1

            if nums[p3] == target:
                return p3
            elif nums[p3] < target:
                p1 = p3 + 1
            else: #nums[p3] > target
                p2 = p3 - 1

        return 0 #fix