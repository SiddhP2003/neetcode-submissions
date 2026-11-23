class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}

        maxLen = 0
        l = 0 

        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1

            while l < r and (r - l + 1) - max(chars.values()) > k:
                chars[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)

        
        return maxLen
