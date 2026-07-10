class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        result = [0] * len(temperatures)
        stk = []

        for i, tmp in enumerate(temperatures):
            if not stk:
                stk.append((tmp, i))

            elif tmp <= stk[-1][0]:
                stk.append((tmp,i))

            else: #need to pop
                while stk and tmp > stk[-1][0]:
                    popped = stk.pop()
                    result[popped[1]] = i - popped[1]

                stk.append((tmp, i))

        return result