from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)

        if nt > ns:
            return ""

        dt = Counter(t)
        ds = Counter()

        for c in dt:
            if c not in s:
                return ""

        l = 0
        r = 0

        required = len(dt)
        formed = 0

        res = ""

        while r < ns:
            c = s[r]

            if c in dt:
                ds[c] += 1
                if ds[c] == dt[c]:
                    formed += 1
            r += 1

            while formed == required:
                if res == "" or r - l < len(res):
                    res = s[l:r]

                c = s[l]

                if c in dt:
                    ds[c] -= 1

                    if ds[c] < dt[c]:
                        formed -= 1
                l += 1

        return res
