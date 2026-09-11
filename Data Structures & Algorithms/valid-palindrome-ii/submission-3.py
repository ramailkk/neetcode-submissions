class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while (l < r):
            if s[l] != s[r]:
                left = s[0:l] + s[l+1: len(s)]
                right = s[0:r] + s[r+1: len(s)]
                return left == left[::-1] or right == right[::-1]
            l += 1
            r -= 1
        return True
