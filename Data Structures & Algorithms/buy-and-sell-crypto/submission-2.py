class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # brute force 
        # start from each day and find the max profit by looking at the days after 
        # return max 
        # O(n^2)

        #optimal solution 
        # sliding window 
        # O(n) Space O(1)
        
        l = 0 
        maxProfit = 0 

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r 
            else:
                maxProfit = max(maxProfit, prices[r] - prices[l])
        
        return maxProfit