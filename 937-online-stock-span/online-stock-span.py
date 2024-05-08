class StockSpanner:

    def __init__(self):
        self.stack = [] #[[span, price]]

    def next(self, price: int) -> int:
        count = 1
        while self.stack and self.stack[-1][1] <= price:
            span, p = self.stack.pop()
            count += span
        self.stack.append([count, price])
        return count
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)