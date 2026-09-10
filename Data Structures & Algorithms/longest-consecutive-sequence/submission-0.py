class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        import heapq
        if len(nums) == 0:
            return 0
        heapq.heapify(nums)
        top = heapq.heappop(nums)
        counter = 1     
        max_counter = counter   
        if len(nums) == 0:
            return counter
        for i in range(len(nums)):
            x = heapq.heappop(nums)
            if top == x:
                continue
            if x - top == 1:
                counter += 1
                max_counter = max(counter, max_counter)
            else:
                counter = 1
            top = x
        return max_counter