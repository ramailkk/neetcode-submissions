class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_arr = set()
        for num in nums:
            hash_arr.add(num)
        
        start_positions = set()
        for num in nums:
            if num - 1 not in hash_arr and num - 1 not in start_positions:
                start_positions.add(num)
        max_counter = 0
        for num in start_positions:
            counter = 1
            while num + 1 in hash_arr:
                counter += 1
                num = num + 1
            max_counter = max(counter, max_counter)

        return max_counter