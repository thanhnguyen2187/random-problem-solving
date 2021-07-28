from typing import (
    List,
    Optional,
    Union,
    NamedTuple,
    Dict,
    Set,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    product,
    accumulate,
    takewhile,
    islice,
    chain,
    cycle,
    repeat,
    permutations,
)
from functools import (
    cached_property,
    # cache,
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


class TreeElement(NamedTuple):
    index: int
    value: int


class Solution:

    def numTrees(
        self,
        n: int,
    ) -> int:

        catalan_numbers = {
            0: 1,
            1: 1,
        }
        for x in range(2, n + 1):
            catalan_numbers[x] = sum(
                catalan_numbers[i] * catalan_numbers[x - 1 - i]
                for i in range(x)
            )

        return catalan_numbers[n]


if __name__ == '__main__':
    solution = Solution()
    for n in [
        3, 4, 5,
    ]:
        print(
            solution.numTrees(n=n)
        )
