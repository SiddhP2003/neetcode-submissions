class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ABAB k = 2
        # brute force 
        # go through the string starting from each character and run until k = 0 and keep track of max length 
        # return max length
        # O(n^2)

        #optimal solution 
        # l,r 
        # "AABABBA"
        # keep track of the count of characters in your current window 
        # keep adding to the window until k < 0 which meants that your window size - count of the character with max length > k 
        # k = 1
        # r - l + 1 : window length
        # A: 2, B: 2, 
        # max = 4
        # "ABBA"
        # Time: O(n)
        # Space: O(n)
        count = {}
        res = 0

        l = 0 
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1 

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res