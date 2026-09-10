class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            a = [0] * 26
            for i in range(len(s)):
                index = ord(s[i].lower()) - 97
                a[index] += 1
            t = tuple(a)
            if t not in d:
                d[t] = [s]
            else:
                d[t].append(s)
        result = []
        for key in d:
            result.append(d[key])
        return result