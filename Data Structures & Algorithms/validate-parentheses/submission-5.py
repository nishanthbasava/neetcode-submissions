class Solution:
    def isValid(self, s: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        stk = []
        pairs = {'[': ']', '{':'}', '(':')'}

        for char in s:
            if not stk: 
                stk.append(char)

            elif pairs.get(stk[-1], 0) == char:
                stk.pop()

            else:
                stk.append(char)

        if stk:
            return False
        return True