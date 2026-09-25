class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)
        if nt > ns:
            return ""
        
        dt = Counter(t)
        ds = Counter(s)

        if dt == ds:
            return s

        
        for c in dt:
            if c not in ds:
                return ""

        l = 0
        r = 0
        
        def is_valid(d) -> bool:
            for c in dt:
                if d[c] < dt[c]:
                    return False
            return True

        if not is_valid(ds):
            return ""

        for c in s:
            ds[c] = 0

        res = s
        formed = 0

        while l <= r and r < ns:
            
            if formed != len(dt):
                if s[r] in dt:
                    dt[s[r]] -= 1
                    if dt[s[r]] == 0:
                        formed += 1
                r += 1            

            while formed == len(dt):
                if len(s[l:r]) < len(res):
                    res = s[l:r]
                if s[l] in dt:
                    dt[s[l]] += 1
                    if dt[s[l]] == 1:
                        formed -=1
                l += 1
        return res
            
