class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'[':']', '{':'}', '(':')'}

        i = 0
        while i < len(s):
            if s[i] in pairs:
                stack.append(s[i])
            elif (len(stack) >= 1) and pairs[stack[-1]] == s[i]:
                stack.pop()
            else:
                return False
            i += 1

        if len(stack) != 0:
            return False
        return True 