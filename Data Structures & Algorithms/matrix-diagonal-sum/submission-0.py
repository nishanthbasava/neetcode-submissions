class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0

        for i, row in enumerate(mat):
            total += row[i]
            total += row[len(mat) - 1 - i]

        if len(mat) % 2 == 1:
            total -= mat[len(mat) // 2][len(mat) // 2]

        return total