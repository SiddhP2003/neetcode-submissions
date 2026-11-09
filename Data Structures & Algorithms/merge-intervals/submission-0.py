class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        #sort intervals by start
        # 1, 3
        # if start value is less than end of last value merge 
        res = []

        intervals.sort(key = lambda x: x[0])

        for interval in intervals:
            start, end = interval[0], interval[1]
            if len(res) > 0 and res[-1][1] >= start:
                nStart = min(start, res[-1][0])
                nEnd = max(end, res[-1][1])
                res.pop()
                res.append([nStart, nEnd])
            else:
                res.append([start, end])
        
        return res