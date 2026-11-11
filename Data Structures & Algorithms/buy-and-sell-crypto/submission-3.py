class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
                curMax = 0
            else:
                res = max(prices[r] - prices[l], res)
        
        return res