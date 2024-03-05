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


def overlap(interval_1: List[int], interval_2: List[int]):
    i, j = interval_1
    k, l = interval_2
    if i > k:
        i, j, k, l = k, l, i, j

    return i <= k <= j or k <= j <= l


def merge(i1: List[int], i2: List[int]):
    return [
        min(i1[0], i2[0]),
        max(i1[1], i2[1]),
    ]


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        new_intervals = [intervals[0]]

        for interval in intervals[1:]:
            last = new_intervals[-1]
            if overlap(interval_1=interval, interval_2=last):
                new_intervals.pop()
                new_intervals.append(merge(i1=interval, i2=last))
            else:
                new_intervals.append(interval)

        return new_intervals


if __name__ == '__main__':
    solution = Solution()
    # print(solution.insert(
    #     intervals=[[1, 3], [6, 9]],
    #     newInterval=[2, 5],
    # ))
    # print(solution.insert(
    #     intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]],
    #     newInterval=[4, 8],
    # ))
    print(solution.insert(
        intervals=[[1, 5]],
        newInterval=[1, 7],
    ))
