class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #brute force 
        # two for loops 
        # look through every combination
        # O(n^2)

        #optimal solution
        # len(s) == 0 then return 0
        # len(s) == 1 then return 1 
        # two pointers 
        # l,r = 0, 1 
        # maxLength = 0 
        # set to keep track of cur chars 
        # while r < len(s):
        #   while s[r] in set:
        #       l += 1 
        #       remove s[l] from set
        #   
        #   add s[r] to set 
        #   maxLength = max(maxLength, set length)
        #   r += 1

        charSet = set()
        l = 0
        maxLength = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLength = max(maxLength, r - l + 1)

        return maxLength