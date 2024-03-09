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
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        columns = set()

        for i, j in product(range(m), range(n)):
            if matrix[i][j] == 0:
                rows.add(i)
                columns.add(j)

        for i, j in product(range(m), range(n)):
            if i in rows or j in columns:
                matrix[i][j] = 0


if __name__ == '__main__':
    solution = Solution()
