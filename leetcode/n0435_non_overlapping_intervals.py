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


def overlap(i1, i2):
    i, j = i1
    k, l = i2
    if i > k:
        i, j, k, l = k, l, i, j

    return i <= k < j or k < j <= l


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: (pair[1], pair[0]))
        new_intervals = [intervals[0]]
        count = 0
        for interval in intervals[1:]:
            last = new_intervals[-1]
            if overlap(i1=interval, i2=last):
                count += 1
            else:
                new_intervals.append(interval)

        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.eraseOverlapIntervals(
        intervals=[
            [-52, 31], [-73, -26], [82, 97],
            [-65, -11], [-62, -49], [95, 99],
            [58, 95], [-31, 49], [66, 98],
            [-63, 2], [30, 47], [-40, -26],
        ],
    ))
