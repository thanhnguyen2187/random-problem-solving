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


class Operation(NamedTuple):
    a: int
    b: int


class Solution:

    def maxCount(
        self,
        m: int,
        n: int,
        ops: List[List[int]],
    ) -> int:

        if len(ops) == 0:
            return m * n

        a_min = min(
            op[0]
            for op in ops
        )
        b_min = min(
            op[1]
            for op in ops
        )

        return a_min * b_min


if __name__ == '__main__':
    solution = Solution()
