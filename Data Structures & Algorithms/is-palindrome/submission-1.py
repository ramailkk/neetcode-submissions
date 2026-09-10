class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t = ''
        for i in range(len(s)):
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9'):
                t = t + s[i]
        return t == t[::-1]