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


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def overlap(i1: Interval, i2: Interval):
    if i1.start > i2.start or (i1.start == i2.start and i1.end > i2.end):
        i1, i2 = i2, i1

    return i1.end > i2.start


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: (i.end, i.start))
        rooms = defaultdict(list)

        for i in range(len(intervals)):
            interval = intervals[i]
            j = 0
            while True:
                room = rooms[j]
                if len(room) == 0 or not overlap(i1=interval, i2=room[-1]):
                    room.append(interval)
                    break
                else:
                    j += 1

        return len(rooms)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.minMeetingRooms(intervals=[Interval(0, 40), Interval(5, 10), Interval(15, 20)]))
    print(
        solution.minMeetingRooms(
            intervals=[
                Interval(i, j)
                for i, j in (
                    (0, 10), (10, 20), (20, 30),
                    (30, 40), (40, 50), (50, 60),
                    (60, 70), (70, 80), (80, 90),
                    (90, 100), (0, 100), (10, 90),
                    (20, 80), (30, 70), (40, 60),
                    (50, 50),
                )
            ]
        )
    )
    print(overlap(i1=Interval(50, 60), i2=Interval(50, 50)))
    print(overlap(i1=Interval(50, 50), i2=Interval(50, 60)))
