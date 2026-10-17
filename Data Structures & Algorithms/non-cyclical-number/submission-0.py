class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        seen = set()
        num = 0
        while True:
            for x in s:
                num += int(x)*int(x)
            if num == 1:
                return True
            if num in seen:
                return False
            seen.add(num)
            s = str(num)
            num = 0
        return False
        