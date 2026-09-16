class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        #brute force
        # trying every k value until it is valid 

        low, high = 1, max(piles)
        res = high
        while low <= high:
            k = (low + high) // 2
            totalHours = 0
            for i in range(len(piles)):
                totalHours += (math.ceil(piles[i] / k))
            
            if totalHours <= h:
                res = min(res, k)
                high = k - 1
            else:
                low = k + 1
        
        return res
        
