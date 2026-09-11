class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        limit = min(len(word1), len(word2))
        s = ''
        while p1 < limit or p2 < limit:
            if p1 == p2:
                s = s + word1[p1]
                p1 += 1
            else:
                s = s + word2[p2]
                p2 += 1
        if len(word1) > limit:
            return s + word1[p1: len(word1)]
        elif len(word2) > limit:
            return s + word2[p2: len(word2)]
        return s