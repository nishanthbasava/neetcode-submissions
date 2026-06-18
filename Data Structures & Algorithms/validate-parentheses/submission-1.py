class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'[':']', '{':'}', '(':')'}

        i = 0
        while i < len(s):
            stack.append(s[i])
            if (len(stack) >= 2) and (stack[-2] in pairs) and (pairs[stack[-2]] == stack[-1]):
                stack.pop()
                stack.pop()
            i += 1

        if len(stack) != 0:
            return False
        return True 