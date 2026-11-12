class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        curStr = set()
        l = 0
        for r in range(len(s)):
            while s[r] in curStr:
                curStr.remove(s[l])
                l += 1
            curStr.add(s[r])
            res = max(r - l + 1, res)
        return res