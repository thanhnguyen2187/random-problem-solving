from typing import (
    DefaultDict,
    Dict,
    Iterator,
    List,
    NamedTuple,
    Optional,
    Set,
    Tuple,
    Union,
    Iterable,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    accumulate,
    chain,
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


def calculate_adjacent_coordinates(x: int, y: int, row_count: int, column_count: int) -> Iterable[Tuple[int, int]]:
    return {
        *(
            (x, y_)
            for y_ in range(row_count)
        ),
        *(
            (x_, y)
            for x_ in range(column_count)
        )
    }


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        column_count = len(grid[0])

        connected_count = 0

        for y, x in product(range(row_count), range(column_count)):
            if grid[y][x] == 0:
                continue

            adjacent_coordinates = calculate_adjacent_coordinates(
                x=x, y=y,
                row_count=row_count,
                column_count=column_count,
            )
            valid_coordinates = tuple(
                (x, y)
                for x, y in adjacent_coordinates
                if grid[y][x] == 1
            )
            if len(valid_coordinates) > 1:
                connected_count += 1

        return connected_count


if __name__ == '__main__':
    solution = Solution()
    # print(solution.countServers(grid=[[1, 0], [0, 1]]))
    # print(solution.countServers(grid=[[1, 0], [1, 1]]))
    # print(solution.countServers(grid=[[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
    # print(solution.countServers(grid=[[1, 0, 0, 1, 0],
    #                                   [0, 0, 0, 0, 0],
    #                                   [0, 0, 0, 1, 0]]))
    # print(solution.countServers(grid=[[0, 0, 0, 0],
    #                                   [1, 1, 1, 1],
    #                                   [0, 0, 0, 1],
    #                                   [0, 0, 1, 1],
    #                                   [0, 0, 0, 1]]))
    print(solution.countServers(grid=[[0, 0, 0, 1, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 1, 1, 0, 0],
                                      [0, 1, 1, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0, 0, 0],
                                      [0, 1, 0, 1, 0, 0, 1, 0, 0]]))
