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


class Pair(NamedTuple):
    duration: int
    character: str


class Solution:

    def slowestKey(
        self,
        releaseTimes: List[int],
        keysPressed: str,
    ) -> str:

        pairs = [
            Pair(
                character=keysPressed[0],
                duration=releaseTimes[0],
            )
        ]

        for index in range(1, len(releaseTimes)):
            pairs.append(
                Pair(
                    character=keysPressed[index],
                    duration=releaseTimes[index] - releaseTimes[index - 1],
                )
            )

        return max(pairs).character


if __name__ == '__main__':
    solution = Solution()
    for releaseTimes, keysPressed in [
        ([23, 34, 43, 59, 62, 80, 83, 92, 97], "qgkzzihfc"),
    ]:
        print(
            solution.slowestKey(
                releaseTimes=releaseTimes,
                keysPressed=keysPressed,
            )
        )
