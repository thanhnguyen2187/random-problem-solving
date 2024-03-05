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


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def overlap(i1: Interval, i2: Interval):
    if i1.start > i2.start:
        i1, i2 = i2, i1

    return i1.end <= i2.start


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: (i.start, i.end))
        i = 0
        while i < len(intervals) - 1:
            j = i + 1
            if overlap(i1=intervals[i], i2=intervals[j]):
                return False
            i += 1

        return True


if __name__ == '__main__':
    solution = Solution()
