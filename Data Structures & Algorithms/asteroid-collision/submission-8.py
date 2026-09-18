class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        i = 0
        for i in range(len(asteroids)):
            cur = asteroids[i]
            if len(s) == 0:
                s.append(cur)
                continue
            if cur ^ s[-1] < 0:
                top = s.pop()
                if top < 0:
                    s.append(top)
                    s.append(cur)
                    continue
                p = 0
                if abs(top) > abs(cur):
                    p = top
                elif abs(cur) > abs(top):
                    p = cur
                else:
                    continue
                if p < 0:
                    while len(s) > 0 and s[-1] > 0 and p < 0:
                        top = s.pop()
                        if abs(top) > abs(p):
                            p = top
                        elif abs(p) > abs(top):
                            continue
                        else:
                            p = 0
                            break
                if p != 0:
                    s.append(p)
            else:
                s.append(cur)
        return s 