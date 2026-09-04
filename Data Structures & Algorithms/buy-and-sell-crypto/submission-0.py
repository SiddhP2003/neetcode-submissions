class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force 
        # two for loops to try every combination
        # O(n^2)

        #optimal solution
        if len(prices) == 1:
            return 0
        l,r = 0, 1
        maxProfit = 0 
        # 0, 4, 5
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                maxProfit = max(prices[r] - prices[l], maxProfit)
            elif prices[l] >= prices[r]:
                l = r

        return maxProfit
        
