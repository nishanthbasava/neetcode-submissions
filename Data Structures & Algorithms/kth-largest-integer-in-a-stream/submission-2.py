import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.capacity = k
        for num in nums:
            self.add(num)

        print(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) == self.capacity and self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        elif len(self.heap) < self.capacity:
            heapq.heappush(self.heap, val)

        return self.heap[0]