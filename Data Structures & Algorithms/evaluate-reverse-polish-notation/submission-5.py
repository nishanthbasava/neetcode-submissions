class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stk.append(int(token))
            else: #is an operation
                y = stk.pop()
                print("y: " + str(y))
                x = stk.pop()
                print("x: " + str(x))

                if token == "+":
                    stk.append(x + y)
                elif token == "-":
                    stk.append(x - y)
                elif token == "*":
                    stk.append(x * y)
                else: #division
                    stk.append(int(x / y))

        return stk[0]