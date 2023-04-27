from typing import (
    DefaultDict,
    Dict,
    Iterator,
    List,
    NamedTuple,
    Optional,
    Set,
    Union,
    Callable,
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


def is_land(grid, x, y) -> bool:
    return grid[x][y] == 1


def find_next_cells(grid, marker, x, y, m, n) -> List:
    return [
        (i, j)
        for i, j in [
            (x + 1, y),
            (x, y + 1),
            (x - 1, y),
            (x, y - 1),
        ]
        if (
            (i, j) not in marker and
            0 <= i < m and
            0 <= j < n and
            is_land(grid=grid, x=i, y=j)
        )
    ]


def is_boundary_cell(x: int, y: int, m: int, n: int) -> bool:
    return (
        (x == 0 or x == m - 1)
        or (y == 0 or y == n - 1)
    )


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        marker = set()
        result = 0
        for x, y in product(range(m), range(n)):
            if (
                is_land(grid=grid, x=x, y=y)
                and (x, y) not in marker
            ):
                marker.add((x, y))

                # bfs
                island_cells = [(x, y)]
                dq = deque([(x, y)])
                while len(dq) > 0:
                    x, y = dq.pop()
                    next_cells = find_next_cells(
                        grid=grid,
                        marker=marker,
                        x=x, y=y,
                        m=m, n=n,
                    )
                    marker.update(next_cells)
                    island_cells.extend(next_cells)
                    dq.extendleft(next_cells)

                if not any(
                    is_boundary_cell(x=x, y=y, m=m, n=n)
                    for x, y in island_cells
                ):
                    result += len(island_cells)
        return result


if __name__ == '__main__':
    solution = Solution()
    # print(
    #     solution.numEnclaves(
    #         grid=[
    #             [0, 0, 0, 0],
    #             [1, 0, 1, 0],
    #             [0, 1, 1, 0],
    #             [0, 0, 0, 0],
    #         ],
    #     )
    # )
    print(
        solution.numEnclaves(
            grid=[
                [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
                [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
                [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
                [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
                [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
                [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            ]
        )
    )
