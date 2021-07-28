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
        nodes_dict: DefaultDict[int, List[int]],
    ):
        nodes_queue = defaultdict(deque)
        nodes_queue[0].append(root)

        level_current = 0
        level_max = 0
        while level_current <= level_max:

            node: TreeNode
            if level_current % 2 == 1:
                node = nodes_queue[level_current].pop()
            else:
                node = nodes_queue[level_current].popleft()

            if node is not None:
                nodes_dict[level_current].append(node.val)
                nodes_queue[level_current + 1].append(node.left)
                nodes_queue[level_current + 1].append(node.right)

                level_max = max(
                    level_current + 1,
                    level_max,
                )

            if len(nodes_queue[level_current]) == 0:
                level_current += 1


    def zigzagLevelOrder(
        self,
        root: TreeNode,
    ) -> List[List[int]]:
        nodes_dict = defaultdict(list)

        self.traverse(
            root=root,
            # level=0,
            # counter=0,
            nodes_dict=nodes_dict,
        )

        return list(
            nodes_dict.values(),
        )


if __name__ == '__main__':
    solution = Solution()
