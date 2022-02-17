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

    def count_good_nodes(
        self,
        root: TreeNode,
        traversed_max: int,
    ) -> int:

        if root is None:
            return 0

        current_max = max(
            traversed_max,
            root.val
        )
        return (
            (
                1
                if root.val >= current_max
                else 0
            ) + (
                self.count_good_nodes(
                    root=root.left,
                    traversed_max=current_max,
                ) +
                self.count_good_nodes(
                    root=root.right,
                    traversed_max=current_max,
                )
            )
        )

    def goodNodes(
        self,
        root: TreeNode,
    ) -> int:

        return self.count_good_nodes(
            root=root,
            traversed_max=root.val,
        )


if __name__ == '__main__':
    solution = Solution()
