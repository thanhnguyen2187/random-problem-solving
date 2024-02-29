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
    combinations,
    cycle,
    islice,
    permutations,
    product,
    repeat,
    takewhile,
)
from functools import (
    cache,
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurse(root: TreeNode, bound_left: int, bound_right: int) -> bool:
            return (
                bound_left < root.val < bound_right
            ) and (
                recurse(
                    root=root.left,
                    bound_left=bound_left,
                    bound_right=min(bound_right, root.val),
                )
                if root.left is not None
                else True
            ) and (
                recurse(
                    root=root.right,
                    bound_left=max(bound_left, root.val),
                    bound_right=bound_right,
                )
                if root.right is not None
                else True
            )

        if root is None:
            return True

        return recurse(root=root, bound_left=float("-inf"), bound_right=float("inf"))


if __name__ == '__main__':
    solution = Solution()
