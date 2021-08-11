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

    def is_same_tree(
        self,
        root_1: TreeNode,
        root_2: TreeNode,
    ) -> bool:
        if (
            root_1 is None or
            root_2 is None
        ):
            return (
                root_1 is None and
                root_2 is None
            )

        return (
            root_1.val == root_2.val and
            self.is_same_tree(
                root_1=root_1.left,
                root_2=root_2.left,
            ) and
            self.is_same_tree(
                root_1=root_1.right,
                root_2=root_2.right,
            )
        )

    def isSameTree(
        self,
        p: TreeNode,
        q: TreeNode,
    ) -> bool:
        return self.is_same_tree(
            root_1=p,
            root_2=q,
        )


if __name__ == '__main__':
    solution = Solution()
