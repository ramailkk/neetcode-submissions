class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        m = 0

        while l <= r and r < len(prices):
            if l == r:
                r += 1
            elif prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                m = max(profit, m)
                r += 1
        return m