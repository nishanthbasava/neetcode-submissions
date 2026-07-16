import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.used = 0
        self.capacity = k
        for num in nums:
            self.add(num)

        print(self.heap)

    def add(self, val: int) -> int:
        if self.used == self.capacity and self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        elif self.used < self.capacity:
            heapq.heappush(self.heap, val)
            self.used += 1

        return self.heap[0]