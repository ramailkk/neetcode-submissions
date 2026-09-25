from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)

        if nt > ns or t == "":
            return ""

        dt = Counter(t)

        l = 0
        r = 0
        need = len(dt)
        have = 0
        res, resLen = "", float("infinity")

        window = {}

        for r in range(ns):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in dt and window[c] == dt[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in dt and window[s[l]] < dt[s[l]]:
                    have -= 1
                l += 1

        return res if resLen != float("infinity") else ""
