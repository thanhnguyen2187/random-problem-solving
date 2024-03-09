import bisect

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
    bisect_left,
    bisect_right,
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
    cache,
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class MedianFinder:

    def __init__(self):
        self.list_ = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.list_, num)

    def findMedian(self) -> float:
        n = len(self.list_)
        i = n // 2

        if n % 2 == 0:
            return (self.list_[i] + self.list_[i + 1]) / 2

        return self.list_[i]


if __name__ == '__main__':
    solution = Solution()
