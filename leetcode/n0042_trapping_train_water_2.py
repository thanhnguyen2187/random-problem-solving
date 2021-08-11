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

    def trap(
        self,
        heights: List[int],
    ) -> int:

        n = len(heights)
        if n == 0:
            return 0

        index_left = 0
        index_right = n - 1
        max_left = heights[0]
        max_right = heights[n - 1]
        accumulated = 0

        def take_positive(x: int) -> int:
            return (
                0
                if x < 0
                else x
            )

        while index_left < index_right:
            if max_left < max_right:
                index_left += 1
                accumulated += take_positive(max_left - heights[index_left])
                max_left = max(
                    max_left,
                    heights[index_left]
                )
            else:
                index_right -= 1
                accumulated += take_positive(max_right - heights[index_right])
                max_right = max(
                    max_right,
                    heights[index_right]
                )

        return accumulated


if __name__ == '__main__':
    solution = Solution()
    for heights in [
        [],
        # [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        # [4, 2, 0, 3, 2, 5],
    ]:
        print(
            solution.trap(
                heights=heights,
            )
        )
