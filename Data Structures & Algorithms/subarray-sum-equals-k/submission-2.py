class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #O(n) time complexity
        #O(n) space complexity

        psum_to_freq = {0:1}
        running = 0
        count = 0

        for num in nums:
            running += num
            count += psum_to_freq.get(running - k, 0)
            print(num)

            psum_to_freq[running] = psum_to_freq.get(running, 0) + 1
        print(psum_to_freq)
        return count
            

        
        #brute force (O(n^2))
        '''
        count = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]

                if total == k:
                    count += 1

        return count
        '''