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

    def insert(
        self,
        root: Optional[TreeNode],
        value: int,
    ):
        if root is None:
            return TreeNode(val=value)

        if value < root.val:
            root.left = self.insert(root=root.left, value=value)
        elif value >= root.val:
            root.right = self.insert(root=root.right, value=value)

        root = self.balance(root=root)
        return root

    def balance(
        self,
        root: Optional[TreeNode],
    ) -> TreeNode:

        if root is not None:
            if (
                root.left is None and
                root.right is not None and
                root.right.right is not None
            ):
                root_new = root.right
                root
                return root.right


    def sortedListToBST(
        self,
    ) -> int:
        ...


if __name__ == '__main__':
    solution = Solution()
