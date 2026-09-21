class Solution:
    from collections import defaultdict
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        d = Counter(s1)
        d2 = defaultdict(int) 
        c = 0
        l = -1
        r = 0

        while l < r and r < len(s2):
            cur = s2[r]
            if cur in d and d2[cur] + 1 <= d[cur]:
                c += 1
                d2[cur] += 1
                if l == -1 or l == r:
                    l = r
            elif cur not in d:
                
                c = 0
                l = -1
                d2 = defaultdict(int)
            else:
                while d2[cur] >= d[cur]:
                    d2[s2[l]] -= 1
                    c -= 1
                    l += 1

                d2[cur] += 1
                c += 1


            r += 1
            if c == len(s1):
                return True
        return False