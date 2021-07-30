from typing import (
    List,
    Optional,
    Union,
    NamedTuple,
    Dict,
    DefaultDict,
    Set,
    Iterator,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    product,
    cycle,
    repeat,
    islice,
    chain,
    accumulate,
    takewhile,
    permutations,
)
from functools import (
    cached_property,
)
from queue import (
    Queue,
)
from collections import (
    defaultdict,
)


class ListNode:
    def __init__(
            self,
            x: int,
            next: Optional['ListNode'] = None,
    ):
        self.val: int = x
        self.next: 'ListNode' = next


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

    def traverse(
        self,
        root: TreeNode,
        level: int,
        nodes_dict: DefaultDict[int, List[int]]
    ):
        if root is not None:
            nodes_dict[level].append(root.val)
            self.traverse(
                root=root.left,
                level=level + 1,
                nodes_dict=nodes_dict,
            )
            self.traverse(
                root=root.right,
                level=level + 1,
                nodes_dict=nodes_dict,
            )

    def levelOrder(
        self,
        root: TreeNode,
    ) -> List[List[int]]:

        nodes_dict = defaultdict(list)

        self.traverse(
            root=root,
            level=0,
            nodes_dict=nodes_dict,
        )

        return list(nodes_dict.values())


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.levelOrder(
            root=TreeNode(
                val=3,
                left=TreeNode(
                    val=9,
                ),
                right=TreeNode(
                    val=20,
                    left=TreeNode(val=15),
                    right=TreeNode(val=7),
                )
            ),
        )
    )
