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


def alternates():
    while True:
        yield True
        yield False


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        def get_values(p1: tuple, p2: tuple, flag: bool):
            x1, y1 = p1
            x2, y2 = p2
            result = []
            if flag:
                for j in range(y1, y2):
                    result.append(matrix[x1][j])
                for i in range(x1, x2 + 1):
                    result.append(matrix[i][y2])
            else:
                for j in reversed(range(y1 + 1, y2 + 1)):
                    result.append(matrix[x2][j])
                for i in reversed(range(x1, x2 + 1)):
                    result.append(matrix[i][y1])

            return result

        def get_next_points(p1: tuple, p2: tuple, flag: bool):
            i, j = p1
            k, l = p2
            if i == k or j == l:
                return None, None

            if flag:
                return (i + 1, j), (k, l - 1)
            else:
                return (i, j + 1), (k - 1, l)

        p1 = (0, 0)
        p2 = (m - 1, n - 1)
        flags = alternates()
        result = []
        while True:
            flag = next(flags)
            values = get_values(p1=p1, p2=p2, flag=flag)
            result.extend(values)
            p1, p2 = get_next_points(p1=p1, p2=p2, flag=flag)
            if p1 is None:
                break

        return result


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [7, 8, 9],
    ]
    print(solution.spiralOrder(matrix=matrix))
