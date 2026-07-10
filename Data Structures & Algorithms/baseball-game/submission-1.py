class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        stk = []

        for op in operations:
            if op == "+":
                stk.append(int(stk[-1]) + int(stk[-2]))
            elif op == "C":
                stk.pop()
            elif op == "D":
                stk.append(int(stk[-1]) * 2)
            else:
                stk.append(int(op))

        total = 0
        for item in stk:
            total += item

        return total