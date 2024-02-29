import heapq

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        stack = []
        cursor = root

        while cursor is not None and len(stack) > 0:
            while cursor is not None:
                cursor = cursor.left

        return arr[k - 1]


if __name__ == '__main__':
    solution = Solution()
    nodes = [
        TreeNode(1),
        None,
        TreeNode(2),
    ]
    for i in range(len(nodes)):
        l = 2 * i + 1
        r = 2 * i + 2
        if nodes[i] is None:
            continue
        nodes[i].left = (
            nodes[l]
            if l < len(nodes)
            else None
        )
        nodes[i].right = (
            nodes[r]
            if r < len(nodes)
            else None
        )

    result = solution.kthSmallest(root=nodes[0], k=2)
    print(result)
