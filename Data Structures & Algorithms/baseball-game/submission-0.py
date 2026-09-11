class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for i in range(len(operations)):
            op = operations[i]
            if op == "+":
                a = stack.pop()
                b = stack[-1]
                stack.append(a)
                stack.append(a + b)
                total += a + b
            elif op == "C":
                total -= stack.pop()
            elif op == "D":
                d = stack[-1] * 2
                stack.append(d)
                total += d
            else:
                n = int(op)
                stack.append(n)
                total += n
        return total