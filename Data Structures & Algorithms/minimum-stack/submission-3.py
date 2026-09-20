class MinStack:
    m = int
    s = List[int]
    t = List[int]

    def __init__(self):
        self.m = None
        self.s = []
        self.t = []
        
    def push(self, val: int) -> None:
        self.s.append(val)
        if self.m is None:
            self.m = val
        elif val <= self.m:
            self.t.append(self.m)
            self.m = val
        
    def pop(self) -> None:
        if self.s:
            if self.s.pop() == self.m:
                if self.t:
                    self.m = self.t.pop()
                else:
                    self.m = None

            
    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m        
