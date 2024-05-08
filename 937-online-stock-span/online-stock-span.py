class StockSpanner:

    def __init__(self):
        self.hist = []

    def next(self, price: int) -> int:
        count = 1
        for stock in self.hist[::-1]:
            if stock > price:
                break
            else:
                count += 1
        self.hist.append(price)
        return count
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)