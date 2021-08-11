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

    def is_palindrome(
        self,
        characters: List[str],
    ) -> bool:

        index_left = 0
        index_right = len(characters) - 1

        while index_left < index_right:
            if characters[index_left] != characters[index_right]:
                return False

        return True


    def loop(
        self,
        characters: List[str],
    ) -> int:

        n = len(characters)
        results = [
            0
            for _ in range(n)
        ]

        for index_1 in range(1, n):
            for index_2 in range(0, index_1):
                ...

    def minCut(
        self,
        s: str,
    ) -> int:

        return self.loop(
            characters=[
                c
                for c in s
            ]
        )


if __name__ == '__main__':
    solution = Solution()

    for s in [
        "aab",
        "aabb"
    ]:
        print(
            solution.minCut(s=s)
        )
