class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        import math

        heap = []

        for point in points:
            distance = - math.sqrt(point[0]**2 + point[1]**2)

            if len(heap) < k:
                heapq.heappush(heap, (distance, point))

            else:
                if heap[0][0] < distance: # new point is closer than current farthest
                    heapq.heapreplace(heap, (distance, point))
        
        output = []
        for point in heap:
            output.append(point[1])

        return output