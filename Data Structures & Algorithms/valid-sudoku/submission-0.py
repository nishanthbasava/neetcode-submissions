class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        for _ in range(9): 
            rows[_] = set()
        
        cols = {}
        for _ in range(9):
            cols[_] = set()

        regions = {}
        for i in range(3):
            for j in range(3):
                regions[(i,j)] = set()

        for i in range(9): #rows
            for j in range(9): #cols
                val = board[i][j]

                if val == ".":
                    continue

                box = (i // 3, j // 3)

                if (val in rows[i]) or (val in cols[j]) or (val in regions[box]):
                    return False

                rows[i].add(val)
                cols[j].add(val)
                regions[box].add(val)

        return True