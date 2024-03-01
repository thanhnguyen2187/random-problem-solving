import math
import pprint
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


def chunk(lst, n):
    chunk_size = math.ceil(len(lst) / n)
    return [
        lst[i: min(i+chunk_size, len(lst))]
        for i in range(0, len(lst), chunk_size)
    ]


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = defaultdict(lambda: False)
        diags_1 = defaultdict(lambda: False)
        diags_2 = defaultdict(lambda: False)

        result = []
        def recurse(i: int, current: tuple):
            if len(current) == n:
                result.append(current)
                return

            for j in range(n):
                if (
                    cols[j] is False and
                    diags_1[i - j] is False and
                    diags_2[i + j] is False
                ):
                    new_current = (*current, (i, j))
                    cols[j] = True
                    diags_1[i - j] = True
                    diags_2[i + j] = True
                    recurse(i=i + 1, current=new_current)
                    cols[j] = False
                    diags_1[i - j] = False
                    diags_2[i + j] = False

        recurse(i=0, current=())

        boards = []
        for result_ in result:
            board = [
                'Q' if (i, j) in result_
                else '.'
                for i, j in product(range(n), range(n))
            ]
            board = chunk(lst=board, n=n)
            board = [
                ''.join(row)
                for row in board
            ]
            boards.append(board)

        return boards


if __name__ == '__main__':
    solution = Solution()
    pprint.pprint(solution.solveNQueens(n=4))
