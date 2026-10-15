class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums) # each value is product of values before
        suffix_product = [1] * len(nums) # each value is product of values after

        #prefix pass
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            prefix_product[i] = product

        #suffix pass
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            suffix_product[i] = product

        #product pass
        return [prefix_product[i] * suffix_product[i] for i in range(len(nums))]


        #handle 0s later