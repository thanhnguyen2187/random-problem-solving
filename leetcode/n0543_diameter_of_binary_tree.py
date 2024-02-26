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
    cached_property,
    cache,
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        @cache
        def recurse_maximal_depth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            return 1 + max(
                recurse_maximal_depth(root=root.left),
                recurse_maximal_depth(root=root.right),
            )

        def recurse(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            return max(
                (
                    recurse_maximal_depth(root=root.left)
                    if root.left is not None
                    else 0
                ) + (
                    recurse_maximal_depth(root=root.right)
                    if root.right is not None
                    else 0
                ),
                recurse(root=root.left),
                recurse(root=root.right),
            )

        return recurse(root=root)


if __name__ == '__main__':
    solution = Solution()
