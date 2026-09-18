class StockSpanner:
    a : List(int)

    def __init__(self):
        self.a = []

    def next(self, price: int) -> int:
        con = 1
        if not self.a:
            self.a.append(price)
            return con
        for num in reversed(self.a):
            if num <= price:
                con += 1
            else:
                break
        self.a.append(price)
        return con

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)