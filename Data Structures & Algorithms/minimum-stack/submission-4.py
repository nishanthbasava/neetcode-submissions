class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk = []

    def push(self, val: int):
        self.stk.append(val)
        self.minStk.append(min(self.minStk[-1], val) if self.minStk else val)

    def pop(self):
        self.stk.pop()
        self.minStk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1]