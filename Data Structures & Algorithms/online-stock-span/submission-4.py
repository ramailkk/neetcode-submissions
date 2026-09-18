class StockSpanner:
    s : List[int]

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        con = 1
        while self.s and self.s[-1][0] <= price:
            con += self.s[-1][1]
            self.s.pop()
        self.s.append((price,con))
        return con

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)