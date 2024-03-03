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
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        all_os_ = {
            (i, j)
            for i, j in product(range(m), range(n))
            if board[i][j] == "O"
        }
        origin_os = {
            (i, j)
            for i, j in all_os_
            if i == 0 or j == 0 or i == m - 1 or j == n - 1
        }
        expanded_os = set()
        for origin_o in origin_os:
            dq = deque([origin_o])
            while len(dq) > 0:
                i, j = dq.pop()
                expanded_os.add((i, j))

                for k, l in (
                    (i + 1, j),
                    (i - 1, j),
                    (i, j + 1),
                    (i, j - 1),
                ):
                    if (
                        0 <= k < m and
                        0 <= l < n and
                        board[k][l] == "O" and
                        (k, l) not in expanded_os
                    ):
                        dq.append((k, l))

        for i, j in all_os_.difference(expanded_os):
            board[i][j] = "X"

        ...


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve(
        board=[
            ["X", "O", "X", "X"],
            ["X", "O", "X", "X"],
            ["O", "X", "O", "X"],
            ["X", "O", "X", "O"],
        ]
    ))
