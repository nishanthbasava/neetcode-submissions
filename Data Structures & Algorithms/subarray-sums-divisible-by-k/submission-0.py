class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_mod_to_freq = {0:1}
        running_mod = 0
        count = 0

        for num in nums: 
            running_mod = (running_mod + num) % k
            
            count += prefix_mod_to_freq.get(running_mod, 0)

            prefix_mod_to_freq[running_mod] = prefix_mod_to_freq.get(running_mod, 0) + 1

        return count

            
