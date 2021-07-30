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


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.originals = {}
        self.derivatives: DefaultDict[str, int] = defaultdict(lambda: 0)

    def insert(self, key: str, val: int) -> None:
        self.originals[key] = val

    def sum(self, prefix: str) -> int:
        return sum(
            (
                value
                for key, value in self.originals.items()
                if key.startswith(prefix)
            )
        )


class Solution:

    def f(
        self,
    ) -> int:
        ...


if __name__ == '__main__':
    solution = Solution()
    mapsum = MapSum()
    mapsum.insert(
        key="apple",
        val=3,
    )
    print(
        mapsum.sum("apple")
    )
    mapsum.insert(
        key="app",
        val=2,
    )
    print(
        mapsum.sum("ap")
    )

