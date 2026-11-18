class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key= lambda x:x[0])
        res = []

        for interval in intervals:
            start,end = interval[0], interval[1]

            if len(res) > 0 and res[-1][1] >= start:
                nStart = min(res[-1][0], start)
                nEnd = max(res[-1][1], end)

                res.pop()
                res.append([nStart, nEnd])
            else:
                res.append([start, end])
        
        return res