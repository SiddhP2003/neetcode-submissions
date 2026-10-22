class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        count = [0]  * 101

        res = 0
        for h in heights:
            count[h] += 1
        
        i = 0
        for h in range(1, 101):
            c = count[h]
            for j in range(c):
                if heights[i] != h:
                    res += 1
                i += 1

        return res