from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.hashmap = {} # key -> [(timestamp, value)]

    def set(self, key: str, val: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append((timestamp, val))
        else:
            self.hashmap[key] = [(timestamp, val)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashmap:
            i = bisect_right(self.hashmap[key], timestamp, key=lambda pair: pair[0]) - 1
            if i >= 0 and i < len(self.hashmap[key]):
                return self.hashmap[key][i][1]
        return ""