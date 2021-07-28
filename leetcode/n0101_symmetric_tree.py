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

    def is_symmetric(
        self,
        node_left: TreeNode,
        node_right: TreeNode,
    ) -> bool:

        if (
            node_left is None and
            node_right is None
        ):
            return True
        elif (
            node_left is None or
            node_right is None
        ):
            return False
        else:
            return all(
                (
                    node_left.val == node_right.val,
                    self.is_symmetric(
                        node_left=node_left.left,
                        node_right=node_right.right,
                    ),
                    self.is_symmetric(
                        node_left=node_right.left,
                        node_right=node_left.right,
                    ),
                )
            )

    def isSymmetric(
        self,
        root: TreeNode,
    ) -> int:
        return self.is_symmetric(
            node_left=root.left,
            node_right=root.right,
        )


if __name__ == '__main__':
    solution = Solution()
