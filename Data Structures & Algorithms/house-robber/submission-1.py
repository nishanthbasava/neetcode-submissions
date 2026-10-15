class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        highest = 0

        for i, num in enumerate(nums):
            if i - 2 >= 0:
                if i - 3 >= 0:
                    val = max(memo[i-2], memo[i-3]) + num
                else: 
                    val = memo[i-2] + num
            else: 
                val = num
            memo[i] = val

            highest = max(highest, val)


        return highest
