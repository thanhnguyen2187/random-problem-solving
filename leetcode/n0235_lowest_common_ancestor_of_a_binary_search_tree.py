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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse(root: TreeNode, p: TreeNode, q: TreeNode):
            if root.val == p.val or root.val == q.val:
                return root

            if p.val < root.val < q.val:
                return root
            if q.val < root.val:
                return recurse(root=root.left, p=p, q=q)
            if root.val < p.val:
                return recurse(root=root.right, p=p, q=q)

        if p.val > q.val:
            p, q = q, p

        return recurse(root=root, p=p, q=q)


if __name__ == '__main__':
    solution = Solution()
    nodes = [
        TreeNode(6),
        TreeNode(2),
        TreeNode(8),
        TreeNode(0),
        TreeNode(4),
        TreeNode(7),
        TreeNode(9),
        None,
        None,
        TreeNode(3),
        TreeNode(5),
        None,
        None,
        None,
        None,
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

    result = solution.lowestCommonAncestor(root=nodes[0], p=nodes[4], q=nodes[5])
    print(result.val)
