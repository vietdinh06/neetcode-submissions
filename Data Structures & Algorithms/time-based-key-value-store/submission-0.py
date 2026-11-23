class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = [[value, timestamp]]
        else:
            self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.time_map:
            return ""

        result = self.time_map[key]

        l = 0
        r = len(result) - 1
        res = ""

        while l <= r:
            
            mid = l + (r - l) // 2

            time = result[mid][1]
            value = result[mid][0]

            if time < timestamp:
                l = mid + 1
                res = value

            elif time > timestamp:
                r = mid - 1

            else:
                return value

        return res

            

        
