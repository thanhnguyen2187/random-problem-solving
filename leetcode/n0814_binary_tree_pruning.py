from typing import (
    List,
    Optional,
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

    def has_one(
        self,
        node: Optional[TreeNode],
    ):
        if node is None:
            return False
        else:
            return any(
                (
                    node.val == 1,
                    self.has_one(node=node.left),
                    self.has_one(node=node.right),
                )
            )

    def prune(
        self,
        root: TreeNode,
    ):
        if root is not None:
            if self.has_one(node=root.left):
                self.prune(root=root.left)
            else:
                root.left = None
            if self.has_one(node=root.right):
                self.prune(root=root.right)
            else:
                root.right = None

    def pruneTree(
        self,
        root: TreeNode,
    ) -> TreeNode:
        pre_root = TreeNode(val=1, left=root)
        self.prune(root=pre_root)
        return pre_root.left


if __name__ == '__main__':
    solution = Solution()
