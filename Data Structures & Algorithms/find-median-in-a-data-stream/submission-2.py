import heapq
class MedianFinder:

    def __init__(self):
        self.maxheap = [] # lower half
        self.minheap = [] # upper half

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return (self.minheap[0] + (-self.maxheap[0])) / 2

    def addNum(self, num: int) -> None:
        cur_median = self.findMedian() if self.maxheap else float('inf')

        if (num < cur_median):
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

        while (abs(len(self.maxheap) - len(self.minheap)) >= 2):
            if (len(self.maxheap) > len(self.minheap)):
                tmp = -heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, tmp)
            else:
                tmp = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -tmp)