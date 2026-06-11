class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        values_sorted = sorted(freq.items(), key=lambda pair:pair[1], reverse=True)

        output = []

        for i in range(k):
            output.append(values_sorted[i][0])
        
        return output