from typing import (
    DefaultDict,
    Dict,
    Iterator,
    List,
    NamedTuple,
    Optional,
    Set,
    Union,
)
from bisect import (
    bisect,
    bisect_left,
    bisect_right,
    insort,
)
from itertools import (
    accumulate,
    chain,
    combinations,
    cycle,
    islice,
    permutations,
    product,
    repeat,
    takewhile,
)
from functools import (
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class TimeMap:

    def __init__(self):
        self.map = defaultdict(
            lambda: [],
        )

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        list_ = self.map[key]
        if len(list_) == 0:
            return ""

        result = ""
        index_left = 0
        index_right = len(list_) - 1

        while index_left <= index_right:
            index_middle = (index_left + index_right) // 2
            timestamp_middle, value_middle = list_[index_middle]

            if timestamp_middle <= timestamp:
                result = value_middle
                index_left = index_middle + 1
            else:
                index_right -= 1

        return result


if __name__ == '__main__':
    obj = TimeMap()
    obj.set("love", "high", 10)
    obj.set("love", "low", 20)
    # obj.set("love", "low", 15)
    # obj.set("love", "low", 25)
    print(obj.get("love", 5))
    print(obj.get("love", 10))
    print(obj.get("love", 15))
    print(obj.get("love", 20))
    print(obj.get("love", 25))
