class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1
        while (l < r):
            if (s[l] < 'a' or s[l] > 'z') and (s[l] < '0' or s[l] > '9'):
                l += 1
            elif (s[r] < 'a' or s[r] > 'z') and (s[r] < '0' or s[r] > '9'):
                r -= 1
            elif s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True