class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        phrase = ""
        count = ""

        for char in s:
            if char != "]":
                stk.append(char)

            else:
                while stk[-1] != "[":
                    phrase = stk.pop() + phrase

                stk.pop()  # remove "["

                while stk and stk[-1].isdigit():
                    count = stk.pop() + count

                repetitions = int(count)

                stk.append(phrase * repetitions)

                count = ""
                phrase = ""

        return "".join(stk)
