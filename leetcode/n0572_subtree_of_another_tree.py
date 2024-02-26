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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def recurse_same_tree(root_1: Optional[TreeNode], root_2: Optional[TreeNode]) -> bool:
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
                recurse_same_tree(root_1=root_1.left, root_2=root_2.left)
                and recurse_same_tree(root_1=root_1.right, root_2=root_2.right)
            )

        def recurse(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
            return (
                recurse_same_tree(root_1=root, root_2=sub_root)
                or (
                    recurse(root=root.left, sub_root=sub_root)
                    if root.left is not None
                    else False
                )
                or (
                    recurse(root=root.right, sub_root=sub_root)
                    if root.right is not None
                    else False
                )
            )

        return recurse(root=root, sub_root=subRoot)


if __name__ == '__main__':
    solution = Solution()
