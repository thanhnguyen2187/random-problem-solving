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
    defaultdict,
    deque,
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

    def isValidSerialization(
        self,
        preorder: str,
    ) -> bool:

        nodes = preorder.split(",")
        edges = 1

        for node in nodes:
            edges -= 1
            if edges < 0:
                return False
            if node != "#":
                edges += 2

        return edges == 0


if __name__ == '__main__':
    solution = Solution()
    for preorder in [
        "9,3,4,#,#,1,#,#,2,#,6,#,#"
    ]:
        print(
            solution.isValidSerialization(preorder=preorder)
        )
