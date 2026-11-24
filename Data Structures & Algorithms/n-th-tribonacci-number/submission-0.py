class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        cur1 = 0
        cur2 = 1
        cur3 = 1

        for i in range(3, n + 1):
            cur1, cur2, cur3 = cur2, cur3, cur1 + cur2 + cur3

        return cur3