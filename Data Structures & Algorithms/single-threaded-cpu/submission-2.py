class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq
        
        time = 0
        tasks_heap = []
        
        for i, task in enumerate(tasks):
            tasks_heap.append((task[0], task[1], i))
            #enqueueTime, processingTime, index

        heapq.heapify(tasks_heap) #min enqueue time is first
        ready = []
        order = []

        while tasks_heap or ready:
            time += 1
            
            while tasks_heap and tasks_heap[0][0] <= time:
                (ready_time, proc_time, index) = heapq.heappop(tasks_heap)
                heapq.heappush(ready, (proc_time, index))
                
            if ready:
                next_task = heapq.heappop(ready)
                time += next_task[0] - 1
                order.append(next_task[1])

        return order