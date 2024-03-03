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
    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_time = 0
        m = len(grid)
        n = len(grid[0])
        start_oranges = {
            (i, j)
            for i, j in product(range(m), range(n))
            if grid[i][j] == 2
        }
        all_oranges_count = len([
            (i, j)
            for i, j in product(range(m), range(n))
            if grid[i][j] >= 1
        ])
        dq = deque([
            (0, i, j)
            for i, j in start_oranges
        ])
        visited = set()

        while len(dq) > 0:
            time, i, j = dq.popleft()
            if (i, j) in visited:
                # We do this "redundant" check to ensure that time is always
                # minimal. For an exaggerated example, we have two paths to go
                # from (0, 0) to (1, 1):
                #
                # - (0, 0), (0, 1), (1, 1)
                # - (0, 0), (1, 0), (2, 0), (2, 1), (1, 1)
                #
                # The second path is obviously much longer and is going to take
                # 4 units of time comparing to the first path's 2 units of time.
                continue

            visited.add((i, j))
            max_time = max(time, max_time)

            for k, l in (
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ):
                if (
                    0 <= k < m and
                    0 <= l < n and
                    grid[k][l] == 1 and
                    (k, l) not in visited
                ):
                    dq.append((time + 1, k, l))

        if all_oranges_count > len(visited):
            return -1

        return max_time


if __name__ == '__main__':
    solution = Solution()
    # print(solution.orangesRotting(
    #     grid=[
    #         [2, 1, 1],
    #         [1, 1, 0],
    #         [0, 1, 1]
    #     ]
    # ))
    # print(solution.orangesRotting(
    #     grid=[
    #         [2, 1, 1],
    #         [0, 1, 1],
    #         [1, 0, 1]
    #     ]
    # ))
    print(solution.orangesRotting(
        grid=[
            [2, 2],
            [1, 1],
            [0, 0],
            [2, 0],
        ]
    ))
