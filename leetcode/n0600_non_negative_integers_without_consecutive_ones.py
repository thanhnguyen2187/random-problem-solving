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
    cycle,
    repeat,
    islice,
    chain,
    accumulate,
    takewhile,
    permutations,
)
from functools import (
    cached_property,
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

    def generate_pivot(
        self,
        i: int,
    ) -> int:
        return 3 * (2 ** i)

    def findIntegers(
        self,
        n: int,
    ) -> int:
        pivots = []
        i = 0
        while True:
            pivot = self.generate_pivot(i=i)
            if pivot <= n:
                pivots.append(pivot)
            else:
                break
            i += 1

        counter = 0
        for x in range(n + 1):
            if not any(
                (
                    x >= pivot and
                    x & pivot == pivot
                )
                for pivot in pivots
            ):
                counter += 1

        return counter


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.findIntegers(n=5)
    )
