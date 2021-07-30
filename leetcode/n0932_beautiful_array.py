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

    def valid(
        self,
        numbers: List[int],
    ) -> bool:
        if ...:
            ...

    def beautifulArray(
        self,
        n: int,
    ) -> List[int]:

        return self.generate(
            numbers=[
                x
                for x in range(1, n + 1)
            ],
        )


if __name__ == '__main__':
    solution = Solution()

    for n in [
        3, 4, 5, 6, 7, 8
    ]:
        print(
            solution.beautifulArray(n=n),
        )
