class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0 

        l = 0
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                res = max(prices[r] - prices[l], res)
            elif prices[r] < prices[l]:
                l = r 
        

        return res