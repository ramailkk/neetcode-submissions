class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if nums[i] in d:
                return [d[nums[i]],i]
            d[x] = i
        return []