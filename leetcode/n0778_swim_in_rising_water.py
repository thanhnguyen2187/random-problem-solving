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
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        visited = set()
        pq = [(grid[0][0], 0, 0)]
        heapq.heapify(pq)
        result = grid[0][0]
        while len(pq) > 0:
            v, i, j = heapq.heappop(pq)
            if (i, j) in visited:
                continue
            result = max(result, v)
            if (i, j) == (n - 1, n - 1):
                return result

            visited.add((i, j))
            for k, l in (
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ):
                if (
                    (k, l) in visited or
                    not (0 <= k < n and 0 <= l < n)
                ):
                    continue
                heapq.heappush(pq, (grid[k][l], k, l))

        raise Exception('unreachable code')


if __name__ == '__main__':
    solution = Solution()
    # grid = [
    #     [0, 2],
    #     [1, 3],
    # ]
    # grid = [
    #     [0, 1, 2, 3, 4],
    #     [24, 23, 22, 21, 5],
    #     [12, 13, 14, 15, 16],
    #     [11, 17, 18, 19, 20],
    #     [10, 9, 8, 7, 6],
    # ]
    grid = [
        [3, 2],
        [0, 1],
    ]
    print(solution.swimInWater(grid=grid))
