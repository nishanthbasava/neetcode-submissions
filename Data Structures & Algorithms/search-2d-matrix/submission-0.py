class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time Complexity: O(log(m * n))
        # Space Complexity: O(1)

        arr = []

        for row in matrix:
            for num in row:
                arr.append(num)

        p1 = 0 
        p2 = len(arr) - 1

        while p1 <= p2:
            p3 = (p1 + p2) // 2
            if arr[p3] == target:
                return True
            elif arr[p3] > target:
                p2 = p3 - 1
            else:
                p1 = p3 + 1

        return False