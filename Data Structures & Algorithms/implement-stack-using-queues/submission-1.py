from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    # O(n)
    def push(self, x: int) -> None:
        self.q.append(x)

        for item in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    # O(1)
    def pop(self) -> int:
        return self.q.popleft()

    # O(1)
    def top(self) -> int:
        return self.q[0]
    
    # O(1)
    def empty(self) -> bool:
        return not self.q

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()