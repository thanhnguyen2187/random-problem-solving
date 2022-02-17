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


class Streak(NamedTuple):
    character: str
    value: int
    index: int


class Solution:

    def orderlyQueue(
        self,
        s: str,
        k: int,
    ) -> str:

        if k >= 2:
            return "".join(sorted(s))

        n = len(s)
        double_s = "".join(s + s)
        ss = [
            double_s[index:index + n]
            for index in range(n)
        ]

        return min(ss)


if __name__ == '__main__':
    solution = Solution()
    for s, k in [
        ("baacaasdfasdf", 2),
        ("dfasadfjqeqjojasdjkl", 1),
    ]:
        print(
            solution.orderlyQueue(
                s=s,
                k=k,
            )
        )
