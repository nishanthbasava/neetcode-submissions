class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        last = {}

        for i, num in enumerate(nums):
            if num in last and i - last[num] <= k:
                print(num)
                print(i)
                return True

            last[num] = i

        return False