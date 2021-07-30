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
    deque,
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
        nodes_dict: DefaultDict[int, list],
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


    def zigzagLevelOrder(
        self,
        root: TreeNode,
    ) -> List[List[int]]:
        nodes_dict = defaultdict(list)

        self.traverse(
            root=root,
            level=0,
            nodes_dict=nodes_dict,
        )

        return [
            (
                nodes
                if index % 2 == 0
                else (
                    list(reversed(nodes))
                )
            )
            for index, nodes in nodes_dict.items()
        ]


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.zigzagLevelOrder(
            root=TreeNode(
                val=3,
                left=TreeNode(
                    val=9,
                    left=TreeNode(
                        val=8,
                        left=TreeNode(val=4),
                        right=TreeNode(val=2),
                    ),
                    right=TreeNode(
                        val=5,
                        left=TreeNode(val=1),
                        right=TreeNode(val=11),
                    ),
                ),
                right=TreeNode(
                    val=20,
                    left=TreeNode(
                        val=15,
                        left=TreeNode(val=13),
                        right=TreeNode(val=14),
                    ),
                    right=TreeNode(
                        val=7,
                        left=TreeNode(val=9),
                        right=TreeNode(val=21),
                    ),
                )
            ),
        )
    )
