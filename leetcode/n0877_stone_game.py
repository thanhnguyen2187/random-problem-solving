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

    def recurse(
        self,
        piles: List[int],
        sum_a: int,
        sum_b: int,
    ) -> (int, int):

        if len(piles) == 2:
            return (
                max(piles),
                min(piles),
            )

        return (
            sum_a + max(piles[0], piles[-1])
        )

    def stoneGame(
        self,
        piles: List[int],
    ) -> bool:
        ...


if __name__ == '__main__':
    solution = Solution()
