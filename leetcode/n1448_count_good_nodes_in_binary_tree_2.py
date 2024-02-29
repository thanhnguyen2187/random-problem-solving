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
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def recurse(root: Optional[TreeNode], max_so_far: int):
            nonlocal result
            if root is None:
                return

            if root.val >= max_so_far:
                result += 1

            max_so_far = max(max_so_far, root.val)
            recurse(root=root.left, max_so_far=max_so_far)
            recurse(root=root.right, max_so_far=max_so_far)

        recurse(root=root, max_so_far=root.val)
        return result


if __name__ == '__main__':
    solution = Solution()
