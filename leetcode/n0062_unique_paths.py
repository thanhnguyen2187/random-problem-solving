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
    def uniquePaths(self, m: int, n: int) -> int:
        results = [
            [0 for _ in range(n)]
            for _ in range(m)
        ]
        for i in range(m):
            results[i][0] = 1
        for j in range(n):
            results[0][j] = 1

        for i, j in product(range(1, m), range(1, n)):
            results[i][j] = results[i - 1][j] + results[i][j - 1]

        return results[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(m=3, n=7))
