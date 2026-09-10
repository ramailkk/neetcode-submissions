class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        c = {}


        for i in range(0, len(nums)+1):
            c[i] = []

        for key in d:
            c[d[key]].append(key)
        result = []
        limit = k
        for key in reversed(c):
            if k <= 0:
                break
            if  len(c[key]) > 0:
                result.extend(c[key])
                k = k - len(c[key])

        return result[0:limit]