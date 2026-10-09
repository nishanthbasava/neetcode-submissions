class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #now lets lock in and do bfs and dfs

        # Worst-case run time is O(rows x cols)
        #find first one tho
        r0, c0 = 0, 0
        rows, cols = len(grid), len(grid[0])
        perimeter = 0


        while grid[r0][c0] == 0:
            r0 += 1

            if r0 == rows: 
                r0 = 0 
                c0 += 1

        visited = set()

        def dfs(r,c):
            nonlocal perimeter 
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            if grid[r][c] == 0 or (r,c) in visited:
                return

            visited.add((r,c))
            perimeter += 4

            for (dr, dc) in [(0,1), (1,0), (-1,0), (0,-1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    perimeter -= 1


            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(r0, c0)

        return perimeter