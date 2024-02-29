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
    groupby,
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        dq = deque([(root, 0)])
        path = []

        while len(dq) > 0:
            top, level = dq.popleft()
            path.append((top.val, level))

            dq.extend([
                (node, level + 1)
                for node in (top.left, top.right)
                if node is not None
            ])

        result = defaultdict(list)
        for val, level in path:
            result[level].append(val)

        return list(result.values())


if __name__ == '__main__':
    solution = Solution()
    nodes = [
        TreeNode(3),
        TreeNode(9),
        TreeNode(20),
        None,
        None,
        TreeNode(15),
        TreeNode(7),
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

    result = solution.levelOrder(root=nodes[0])
    print(result)
