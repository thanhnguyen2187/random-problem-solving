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
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


def calculate_primary_diagonal_positions(n: int) -> [(int, int)]:
    return (
        (x, x)
        for x in range(0, n)
    )


def calculate_secondary_diagonal_positions(n: int) -> [(int, int)]:
    x, y = n - 1, 0
    while x >= 0:
        yield x, y
        x -= 1
        y += 1


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        result = sum(
            mat[x][y]
            for x, y in calculate_primary_diagonal_positions(n=n)
        )
        result += sum(
            mat[x][y]
            for x, y in calculate_secondary_diagonal_positions(n=n)
        )
        if n % 2 == 1:
            result -= mat[n // 2][n // 2]

        return result


if __name__ == '__main__':
    solution = Solution()
