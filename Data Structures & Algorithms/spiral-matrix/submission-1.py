class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # O(m*n) time and O(1) space

        output = []
        total = len(matrix) * len(matrix[0])
        r_bound = len(matrix) - 1
        c_bound = len(matrix[0]) - 1

        #first row:
        for num in matrix[0]:
            output.append(num)

        row = 0
        col = len(matrix[0]) - 1

        sign = 1 # 1 = positive, -1 = negative

        while len(output) < total:
            print(r_bound)
            print(c_bound)
            for _ in range(r_bound):
                row += sign
                output.append(matrix[row][col])
                
            r_bound -= 1
            sign *= -1

            if len(output) == total:
                break

            for _ in range(c_bound):
                col += sign
                output.append(matrix[row][col])

            c_bound -= 1



        return output