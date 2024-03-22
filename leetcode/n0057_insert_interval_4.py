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


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        result = [intervals[0]]
        for interval in intervals[1:]:
            a = interval
            b = result[-1]
            i, j = a
            k, l = b
            if i > k:
                i, j, k, l = k, l, i, j

            if i <= k <= j:
                result[-1] = [min(i, k), max(j, l)]
            else:
                result.append(a)

        return result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.insert(
    #     intervals=[[1, 3], [6, 9]],
    #     newInterval=[2, 5],
    # ))
    print(solution.insert(
        intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]],
        newInterval=[4, 8],
    ))
    # print(solution.insert(
    #     intervals=[[1, 5]],
    #     newInterval=[1, 7],
    # ))
