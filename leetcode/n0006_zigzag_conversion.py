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
    cached_property,
    partial,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


def generate_changes(num_rows: int) -> Iterator:
    while True:
        # step down
        yield from repeat((1, 0), num_rows - 1)
        # step up right
        yield from repeat((-1, 1), num_rows - 1)


def generate_positions(
    start_position: (int, int),
    num_rows: int,
) -> Iterator:
    changes = generate_changes(num_rows=num_rows)
    current_position = start_position
    while True:
        yield current_position
        change = next(changes)
        x, y = current_position
        change_x, change_y = change
        current_position = (x + change_x, y + change_y)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        positions = generate_positions(start_position=(0, 0), num_rows=numRows)
        s_with_position = list(zip(s, positions))
        s_sorted_by_position = sorted(s_with_position, key=lambda pair: pair[1])
        s_sorted_without_position = list(map(lambda pair: pair[0], s_sorted_by_position))
        result = ''.join(s_sorted_without_position)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.convert(s="PAYPALISHIRING", numRows=3))
    print(solution.convert(s="PAYPALISHIRING", numRows=2))
    print(solution.convert(s="P", numRows=2))
