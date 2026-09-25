class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        heap = []
        res = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k-1:
                while heap:
                    x, j = heap[0]
                    if j > i - k:
                        res.append(-x)
                        break
                    else:
                        heapq.heappop(heap)
        return res