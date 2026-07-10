class MinStack:

    def __init__(self):
        self.stack = []
        self.minStk = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.stack) == 1 or val < self.minStk[-1]:
            self.minStk.append(val)

        else:
            self.minStk.append(self.minStk[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minStk.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStk[-1]