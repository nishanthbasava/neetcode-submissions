class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #O(n) time complexity
        #O(n) space complexity

        record = []

        for op in operations:
            if op == "+":
                record.append(record[-1] + record[-2])
            
            elif op == "C":
                record.pop()

            elif op == "D":
                record.append(record[-1] * 2)

            else:
                record.append(int(op))

        output = 0

        for rec in record:
            output += rec

        return output