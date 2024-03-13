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
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [
            (s, e, p)
            for s, e, p in zip(startTime, endTime, profit)
        ]
        jobs.sort(key=lambda sep: sep[1], reverse=True)

        n = len(jobs)
        ...


if __name__ == '__main__':
    solution = Solution()
    print(solution.jobScheduling(
        startTime=[1, 2, 3, 3],
        endTime=[3, 4, 5, 6],
        profit=[50, 10, 40, 70],
    ))
    # print(solution.jobScheduling(
    #     startTime=[1, 2, 3, 4, 6],
    #     endTime=[3, 5, 10, 6, 9],
    #     profit=[20, 20, 100, 70, 60],
    # ))
    # print(solution.jobScheduling(
    #     startTime=[1, 1, 1],
    #     endTime=[2, 3, 4],
    #     profit=[5, 6, 4],
    # ))
