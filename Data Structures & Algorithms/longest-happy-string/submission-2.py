class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #heapq for prioritizing the highest frequency
        #deque for cool down (which is always 1)

        import heapq

        output = []
        tmp = ""

        heap = [[-count, char] for count, char in [(a, 'a'), (b, 'b'), (c, 'c')] if count > 0]
        heapq.heapify(heap)

        
        while heap:
            if len(output) >= 2 and len(heap) == 1 and heap[0][1] == output[-1] == output[-2]:
                return "".join(output)

            if output and output[-1] == heap[0][1]:
                tmp = heapq.heappop(heap)

            next_char = heapq.heappop(heap)
            output.append(next_char[1])
            next_char[0] += 1

            if not tmp and next_char[0] != 0:
                output.append(next_char[1])
                next_char[0] += 1
                
            if next_char[0] != 0:
                    heapq.heappush(heap, next_char)
            
            if tmp:
                heapq.heappush(heap, tmp)
                tmp = ""

        return "".join(output)