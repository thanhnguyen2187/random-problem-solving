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
)


class ListNode:
    def __init__(
            self,
            x: int,
            next: Optional['ListNode'] = None,
    ):
        self.val: int = x
        self.next: 'ListNode' = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: 'TreeNode' = None,
        right: 'TreeNode' = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Position(NamedTuple):
    index: int
    value: int


class Solution:

    def numDistinct(
        self,
        s: str,
        t: str,
    ) -> int:

        m = len(s)
        n = len(t)
        table = [
            [
                0
                for _ in range(n + 1)
            ]
            for _ in range(m + 1)
        ]

        def set_first_column(index):
            table[index][0] = 1

        list(
            map(
                set_first_column,
                range(0, m + 1),
            )
        )

        for index_1, index_2 in product(
            range(1, m + 1),
            range(1, n + 1),
        ):
            if s[index_1 - 1] == t[index_2 - 1]:
                table[index_1][index_2] = (
                    table[index_1 - 1][index_2 - 1] +
                    table[index_1 - 1][index_2]
                )
            else:
                table[index_1][index_2] = table[index_1 - 1][index_2]

        return table[-1][-1]


if __name__ == '__main__':
    solution = Solution()

    for s, t in [
        ("rabbbit", "rabbit"),
        ("babgbag", "bag"),
        ("acdabefbc", "ab"),
    ]:
        print(
            solution.numDistinct(
                s=s,
                t=t,
            )
        )
