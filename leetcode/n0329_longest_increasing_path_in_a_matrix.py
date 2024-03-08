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
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        @cache
        def recurse(i: int, j: int):
            next_results = [
                recurse(k, l)
                for k, l in (
                    (i, j + 1),
                    (i, j - 1),
                    (i + 1, j),
                    (i - 1, j),
                )
                if (
                    (0 <= k < m and 0 <= l < n) and
                    matrix[i][j] < matrix[k][l]
                )
            ]
            result = 1
            if len(next_results) > 0:
                result += max(next_results)
            return result

        result = 0
        for i, j in product(range(m), range(n)):
            result = max(result, recurse(i, j))

        return result


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1],
    ]
    matrix = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1],
    ]
    print(solution.longestIncreasingPath(matrix=matrix))
