class Solution:
    from collections import defaultdict
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = Counter(s1)
        seen = defaultdict(int)
        c = 0
        l = len(s1)
        for i in range(len(s2)):
            c = 0
            seen.clear()
            for j in range(i,min(len(s2),i+l)):
                cur = s2[j]
                if cur in d and seen[cur] + 1 <= d[cur]:
                    c += 1
                    seen[cur] += 1
                else:
                    break
                if c == l:
                    return True
        return False