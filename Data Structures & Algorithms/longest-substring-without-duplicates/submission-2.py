class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0 
        cur = set()
        l = 0
        for r in range(len(s)):
            while s[r] in cur:
                cur.remove(s[l])
                l += 1
            cur.add(s[r])
            res = max(r - l + 1, res)
        
        return res

