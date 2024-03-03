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
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        not_visited = set(
            (i, j)
            for i, j in product(range(m), range(n))
        )

        result = 0
        while len(not_visited) > 0:
            i, j = not_visited.pop()
            dq = deque()
            if grid[i][j] == '1':
                result += 1
                dq.append((i, j))
            while len(dq) > 0:
                i_, j_ = dq.pop()
                not_visited.discard((i_, j_))

                for k, l in (
                    (i_ + 1, j_),
                    (i_ - 1, j_),
                    (i_, j_ + 1),
                    (i_, j_ - 1),
                ):
                    if (
                        0 <= k < m and
                        0 <= l < n and
                        grid[k][l] == '1' and
                        (k, l) in not_visited
                    ):
                        dq.append((k, l))

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numIslands(
        grid=[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    ))
    print(solution.numIslands(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
    ))
