class Solution:
    def reorganizeString(self, s: str) -> str:
        #heap with highest freq first (so MAX HEAP)
        import heapq

        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) - 1

        heap = [[freq[char], char] for char in freq]
        heapq.heapify(heap)

        output = []
        tmp = None
        while heap:
            if output and len(heap) == 1 and heap[0][1] == output[-1]:
                return ""

            if output and output[-1] == heap[0][1]:
                tmp = heapq.heappop(heap)
            
            next_char = heapq.heappop(heap)
            output.append(next_char[1])
            next_char[0] += 1

            if next_char[0] != 0:
                heapq.heappush(heap, next_char)

            if tmp:
                heapq.heappush(heap, tmp)
                tmp = None
                
        return "".join(output)