class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = 0
        l = 0
        r = len(heights) - 1
        while (l < r):
            height = min(heights[l], heights[r])
            width =  abs(r - l)
            area = height * width
            h = max(area, h)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return h