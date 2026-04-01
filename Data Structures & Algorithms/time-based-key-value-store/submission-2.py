from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        if timestamp < self.time_map[key][0][1]:
            return ""

        l = 0
        r = len(self.time_map[key]) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if timestamp == self.time_map[key][mid][1]:
                return self.time_map[key][mid][0]
            elif timestamp < self.time_map[key][mid][1]:
                r = mid - 1
            else:
                l = mid + 1

        return self.time_map[key][r][0]
