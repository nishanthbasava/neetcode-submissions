from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.hashmap = {} # key -> [(timestamp, value)]

    # relies on the guarantee that timestamps arrive in increasing order
    def set(self, k: str, v: str, ts: int) -> None:
        if k in self.hashmap:
            self.hashmap[k].append((ts, v))
        else:
            self.hashmap[k] = [(ts, v)]

    def get(self, k: str, ts: int) -> str:
        # To do it without bisect_right
        if k in self.hashmap:
            i = bisect_right(self.hashmap[k], ts, key=lambda x:x[0]) - 1
            if i >= 0:
                return self.hashmap[k][i][1]
        return ""
        '''
        if key in self.hashmap:
            arr = self.hashmap[key]
            p1 = 0
            p2 = len(arr)

            

        return ""

        '''