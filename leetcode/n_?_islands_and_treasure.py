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
from collections import (
    defaultdict,
    deque,
    Counter,
)


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        origins = {
            (i, j)
            for i, j in product(range(m), range(n))
            if grid[i][j] == 0
        }

        for i, j in origins:
            dq = deque([(0, i, j)])
            visited = set()
            while len(dq) > 0:
                distance, i, j = dq.popleft()
                visited.add((i, j))
                grid[i][j] = min(grid[i][j], distance)

                for k, l in (
                    (i + 1, j),
                    (i - 1, j),
                    (i, j + 1),
                    (i, j - 1),
                ):
                    if (
                        0 <= k < m and
                        0 <= l < n and
                        (k, l) not in visited and
                        (k, l) not in origins
                        and grid[k][l] != -1
                    ):
                        dq.append((distance + 1, k, l))


if __name__ == '__main__':
    solution = Solution()
