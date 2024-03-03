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
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        not_visited = {
            (i, j)
            for i, j in product(range(m), range(n))
            if grid[i][j] == 1
        }

        max_area = 0
        while len(not_visited) > 0:
            pair = not_visited.pop()
            not_visited.add(pair)
            dq = deque([pair])
            area = 0
            while len(dq) > 0:
                i, j = dq.popleft()
                if (i, j) not in not_visited:
                    continue
                area += 1
                not_visited.remove((i, j))
                for k, l in (
                    (i + 1, j),
                    (i - 1, j),
                    (i, j + 1),
                    (i, j - 1),
                ):
                    if (k, l) in not_visited:
                        dq.append((k, l))
            max_area = max(area, max_area)

        return max_area


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.maxAreaOfIsland(
            grid=[
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
            ]
        )
    )
    print(
        solution.maxAreaOfIsland(
            grid=[
                [1, 1, 1, 0, 0],
                [1, 1, 1, 0, 0],
                [1, 1, 1, 0, 0],
            ]
        )
    )
