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

    def insert_right(
        self,
        root: TreeNode,
        node: TreeNode,
    ):
        if root.right is None:
            root.right = node
        else:
            self.insert_right(
                root=root.right,
                node=node,
            )

    def recurse(
        self,
        root: Optional[TreeNode],
    ):
        if root is None:
            return None

        if root.left is not None:
            self.insert_right(
                root=root.left,
                node=root.right,
            )
            root.right = root.left
            root.left = None

        self.recurse(root=root.right)

    def flatten(
        self,
        root: Optional[TreeNode],
    ) -> None:

        self.recurse(
            root=root,
        )


if __name__ == '__main__':
    solution = Solution()
