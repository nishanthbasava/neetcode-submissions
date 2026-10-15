class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        maximum = 0
        total = 0
        balance_to_index = {0: -1}

        for i, num in enumerate(nums):
            if num == 1:
                total += 1
            else: # num == 0
                total -= 1

            if total in balance_to_index:
                maximum = max(maximum, i - balance_to_index[total])
            else: 
                if total not in balance_to_index:
                    balance_to_index[total] = i

        return maximum




