class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time Complexity: O(m), where m is size of input array
        # Space Complexity: O(1)

        import heapq
        from collections import deque

        freq = {}

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        heap = [[-count, task] for task, count in freq.items()]
        heapq.heapify(heap)

        cooldown = deque()
        time = 0

        while heap or cooldown:
            if cooldown and time >= cooldown[0][0]:
                ready_time, task = cooldown.popleft()
                heapq.heappush(heap, task)
                
            if heap:
                processed = heapq.heappop(heap)
                processed[0] += 1
                
                if processed[0] < 0:
                    cooldown.append((time + n + 1, processed))

            time += 1

        return time