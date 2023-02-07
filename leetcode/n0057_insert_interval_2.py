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
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


def merge_2(interval_1: List[int], interval_2: List[int]) -> List[int]:
    start_1, end_1 = interval_1
    start_2, end_2 = interval_2
    return [
        min([start_1, end_1, start_2, end_2]),
        max([start_1, end_1, start_2, end_2]),
    ]


def overlap(interval_1: List[int], interval_2: List[int]) -> bool:
    start_1, end_1 = interval_1
    start_2, end_2 = interval_2

    return start_2 <= end_1


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = sorted([*intervals, newInterval])

        index = 0
        while index < len(intervals) - 1:
            interval_1 = intervals[index]
            interval_2 = intervals[index + 1]
            if overlap(interval_1=interval_1, interval_2=interval_2):
                merged_interval = merge_2(interval_1=interval_1, interval_2=interval_2)
                intervals = [
                    *intervals[:index],
                    merged_interval,
                    *intervals[index + 2:],
                ]
            else:
                index += 1

        return intervals


if __name__ == '__main__':
    solution = Solution()
    print(solution.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
    print(solution.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
