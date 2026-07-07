class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        #Dynamic sized sliding window

        left = 0
        right = 1

        while left <= len(nums) - 2:
            if nums[left] != nums[right]:
                if right - left < k:
                    right += 1
                else:
                    left += 1

                if right == len(nums):
                    break
            
            else:
                if left != right:
                    return True
                else:
                    right += 1

        return False