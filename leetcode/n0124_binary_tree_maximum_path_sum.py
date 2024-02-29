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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        @cache
        def recurse_max_path_sum(root: Optional[TreeNode]):
            if root is None:
                return 0

            return max(
                root.val,
                root.val + recurse_max_path_sum(root.left),
                root.val + recurse_max_path_sum(root.right),
            )

        def recurse_optimal_path(root: Optional[TreeNode]):
            if root is None:
                return float("-inf")

            return max(
                recurse_max_path_sum(root=root),
                (
                    root.val
                    + recurse_max_path_sum(root=root.left)
                    + recurse_max_path_sum(root=root.right)
                ),
                recurse_optimal_path(root=root.left),
                recurse_optimal_path(root=root.right),
            )

        return recurse_optimal_path(root=root)


if __name__ == '__main__':
    solution = Solution()
