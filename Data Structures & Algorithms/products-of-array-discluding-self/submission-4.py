class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        left = [1] * len(nums)
        right = [1] * len(nums)

        val = 1
        for i in range(1, len(nums)):
            val *= nums[i - 1]
            left[i] = val
        
        val = 1
        for i in range(len(nums) - 1, 0, -1):
            val *= nums[i]
            right[i - 1] = val

        for i in range(0, len(nums)):
            output.append(left[i] * right[i])

        return output