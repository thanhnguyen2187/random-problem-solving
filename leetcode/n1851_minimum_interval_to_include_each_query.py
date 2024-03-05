import heapq

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
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        intervals_ = []
        heapq.heapify(intervals_)
        results_map = defaultdict(lambda: -1)
        j = 0
        for query in sorted(set(queries)):
            while j < len(intervals):
                l, r = intervals[j]
                if l > query:
                    break
                elif l <= query <= r:
                    heapq.heappush(intervals_, (r - l + 1, r))
                j += 1

            while len(intervals_) > 0:
                length, r = intervals_[0]
                if query <= r:
                    results_map[query] = length
                    break
                else:
                    heapq.heappop(intervals_)

        results = [
            results_map[query]
            for query in queries
        ]

        return results

if __name__ == '__main__':
    solution = Solution()
    # print(solution.minInterval(
    #     intervals=[[1, 4], [2, 4], [3, 6], [4, 4]],
    #     queries=[2, 3, 4, 5],
    # ))
    # print(solution.minInterval(
    #     intervals=[[2, 3], [2, 5], [1, 8], [20, 25]],
    #     queries=[2, 19, 5, 22],
    # ))
    print(solution.minInterval(
        intervals=[[4, 5], [5, 8], [1, 9], [8, 10], [1, 6]],
        queries=[7, 9, 3, 9, 3],
    ))
