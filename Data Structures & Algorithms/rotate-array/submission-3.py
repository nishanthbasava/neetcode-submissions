class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k % len(nums)):
            tmp = [nums.pop()]
            nums[:] = tmp + nums