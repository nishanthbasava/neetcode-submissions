'''
Problem: You're given a grid of '0's and '1's. Starting from the top-left cell (0, 0) 
(guaranteed to be '1'), count how many '1' cells are reachable by moving up/down/left/right
through other '1' cells.
'''

grid = [
  ["1","1","0","0"],
  ["0","1","0","1"],
  ["1","1","0","0"],
  ["0","0","0","1"],
]
# Expected output is 5

# ----- My Solution Starts Below: -----

from collections import deque

#FIRST IMPLEMENTATION (with hashset for seen)
def count_reachable(grid: list[list[str]]) -> int:

    R = len(grid)
    C = len(grid[0])
    #if it was specified to be a square grid, just store a single variable "dim"

    (sr, sc) = (0, 0)
    count = 0

    q = deque([(sr, sc)]) # for seen but unprocessed
    visited = {(sr, sc)}

    while q:
        count += 1
        r, c = q.popleft()
        print(f"({r},{c})")

        for (dr, dc) in ((0,1), (1,0), (0,-1), (-1,0)):
            nr, nc = r + dr, c + dc

            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited and grid[nr][nc] == "1":
                visited.add((nr, nc))
                q.append((nr, nc))

    return count


#SECOND IMPLEMENTATION (in place changes to grid)



print(count_reachable(grid))