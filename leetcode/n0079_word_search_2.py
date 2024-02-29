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
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        found = False

        def recurse(i: int, j: int, k: int, visited: set):
            nonlocal found
            if (
                not (0 <= i < m) or
                not (0 <= j < n) or
                (i, j) in visited
            ):
                return

            visited.add((i, j))
            char_board = board[i][j]
            char_word = word[k]
            if char_board == char_word:
                if k == len(word) - 1:
                    found = True
                    return

                for i_, j_ in (
                    (i + 1, j),
                    (i - 1, j),
                    (i, j + 1),
                    (i, j - 1),
                ):
                    recurse(i=i_, j=j_, k=k + 1, visited=visited)

            visited.remove((i, j))

        for i, j in product(range(m), range(n)):
            recurse(i=i, j=j, k=0, visited=set())

        return found


if __name__ == '__main__':
    solution = Solution()
    # print(solution.exist(
    #     board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
    #     word="SEE",
    # ))
    print(solution.exist(
        board=[
            ["a", "b"],
            ["c", "d"],
        ],
        word="cdba",
    ))
