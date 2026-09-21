class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.map.get(key):
            self.map[key] = [[timestamp, value]]
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not self.map.get(key):
            return ""
        res = ""
        l,r = 0, len(self.map[key]) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if self.map[key][mid][0] <= timestamp:
                res = self.map[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res

