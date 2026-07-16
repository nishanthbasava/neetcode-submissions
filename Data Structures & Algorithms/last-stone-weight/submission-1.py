class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)
        
        import heapq

        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone1 = - heapq.heappop(heap)
            stone2 = - heapq.heappop(heap)

            if stone1 != stone2:
                heapq.heappush(heap, - (stone1 - stone2))

        return - heap[0] if len(heap) == 1 else 0
