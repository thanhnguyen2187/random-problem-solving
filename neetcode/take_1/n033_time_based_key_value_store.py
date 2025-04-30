from typing import List
from collections import defaultdict
from bisect import bisect_left


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        left, right = 0, len(values) - 1
        value_min = ""
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                value_min = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return value_min



if __name__ == "__main__":
    time_map = TimeMap()
    # time_map.set("alice", "happy", 1)
    # print(time_map.get("alice", 1))
    # print(time_map.get("alice", 2))
    # time_map.set("alice", "sad", 3)
    # print(time_map.get("alice", 3))
    # time_map.set("foo", "bar", 1)
    # print(time_map.get("foo", 1))
    # print(time_map.get("foo", 3))
    # time_map.set("foo", "bar2", 4)
    # print(time_map.get("foo", 4))
    # print(time_map.get("foo", 5))

    # time_map.set("key1", "value1", 10)
    # print(time_map.get("key1", 1))
