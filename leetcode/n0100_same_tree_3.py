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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recurse(root_1: Optional[TreeNode], root_2: Optional[TreeNode]) -> bool:
            match root_1, root_2:
                case None, None:
                    return True
                case None, _:
                    return False
                case _, None:
                    return False

            if root_1.val != root_2.val:
                return False

            return (
                recurse(root_1=root_1.left, root_2=root_2.left)
                and recurse(root_1=root_1.right, root_2=root_2.right)
            )

        return recurse(root_1=p, root_2=q)


if __name__ == '__main__':
    solution = Solution()
