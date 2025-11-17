class TimeMap(object):

    def __init__(self):
        self.dict = {}

    def set(self, key, value, timestamp):
        if key in self.dict:
            self.dict[key].append((timestamp, value))
        else:
            self.dict[key] = [(timestamp, value)]

    def get(self, key, timestamp):
        if key not in self.dict:
            return ""
        arr = self.dict[key]
        l = 0
        r = len(arr) - 1
        tmp = ""

        while l <= r:
            mid = (l + r) // 2
            t, v = arr[mid]

            if timestamp == t:
                return v
            if t < timestamp:
                tmp = v
                l = mid + 1
            else:
                r = mid - 1

        return tmp