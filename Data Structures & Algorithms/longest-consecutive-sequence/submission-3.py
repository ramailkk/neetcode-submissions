class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_arr = set()
        d = {}
        for num in nums:
            hash_arr.add(num)
            d[num] = num - 1
        
        start_positions = []
        for num in nums:
            if d[num] not in hash_arr:
                start_positions.append(num)
        
        max_counter = 0
        for num in start_positions:
            counter = 1
            while num + 1 in hash_arr:
                counter += 1
                num = num + 1
            max_counter = max(counter, max_counter)

        return max_counter