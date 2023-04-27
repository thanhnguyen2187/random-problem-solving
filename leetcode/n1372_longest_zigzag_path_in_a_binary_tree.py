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


def recurse(
    node: TreeNode,
):
    if node is None:
        return 0, 0
    left = recurse(node.left)[0]
    right = recurse(node.right)[1]


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return recurse(depth=0, node=root, previous_direction=None)


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestZigZag(
        root=TreeNode(
            left=None,
            right=TreeNode(
                left=TreeNode(),
                right=TreeNode(
                    left=TreeNode(
                        right=TreeNode(
                            right=TreeNode(),
                        ),
                    ),
                    right=TreeNode(),
                )
            )
        )
    ))
