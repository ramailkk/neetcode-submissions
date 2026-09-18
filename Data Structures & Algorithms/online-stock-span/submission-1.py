class StockSpanner:
    stack : List(int)

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        con = 1
        if not self.stack:
            self.stack.append(price)
            return con
        temp = []
        while self.stack:
            if self.stack[-1] <= price:
                con += 1
                temp.append(self.stack.pop())
            else:
                break
        while temp:
            self.stack.append(temp.pop())
        self.stack.append(price)
        return con

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)