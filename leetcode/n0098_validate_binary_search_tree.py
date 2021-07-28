from typing import (
    List,
    Optional,
    Union,
    NamedTuple,
    Dict,
    Set,
    Iterator,
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

    def is_valid(
        self,
        root: TreeNode,
        greater: Union[int, float],
        lesser: Union[int, float],
    ):
        return (
            (
                (
                    root.left is not None and
                    lesser < root.left.val < root.val and
                    self.is_valid(
                        root=root.left,
                        greater=min(greater, root.val),
                        lesser=lesser,
                    )
                ) or (
                    root.left is None
                )
            ) and (
                (
                    root.right is not None and
                    root.val < root.right.val < greater and
                    self.is_valid(
                        root=root.right,
                        greater=greater,
                        lesser=max(lesser, root.val),
                    )
                ) or (
                    root.right is None
                )
            )
        )

    def isValidBST(
        self,
        root: TreeNode,
    ) -> bool:
        return self.is_valid(
            root=root,
            greater=float("inf"),
            lesser=float("-inf"),
        )


if __name__ == '__main__':
    solution = Solution()
