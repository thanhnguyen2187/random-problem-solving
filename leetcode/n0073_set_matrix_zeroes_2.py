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


class Solution:

    def setZeroes(
        self,
        matrix: List[List[int]],
    ) -> None:

        m = len(matrix)
        n = len(matrix[0])
        zero_rows = set()
        zero_columns = set()

        for index_1, index_2 in product(
            range(m),
            range(n),
        ):
            if matrix[index_1][index_2] == 0:
                zero_rows.add(index_1)
                zero_columns.add(index_2)

        for index_1, index_2 in product(
            range(m),
            range(n),
        ):
            matrix[index_1][index_2] = (
                0
                if (
                    index_1 in zero_rows or
                    index_2 in zero_columns
                )
                else matrix[index_1][index_2]
            )


if __name__ == '__main__':
    solution = Solution()
