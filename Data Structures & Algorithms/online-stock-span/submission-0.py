class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        count = 1
        i = len(self.stk) - 1
        while i >= 0 and  self.stk[i] <= price:
            count += 1
            i -= 1
        
        self.stk.append(price)
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)