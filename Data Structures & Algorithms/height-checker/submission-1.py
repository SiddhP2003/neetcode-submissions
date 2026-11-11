class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        original = heights.copy()
        heights.sort()
        res = 0
        for i in range(len(original)):
            if original[i] != heights[i]:
                res += 1
        return res