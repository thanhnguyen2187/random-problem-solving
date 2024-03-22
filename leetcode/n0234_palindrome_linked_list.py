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


class ListNode:
    def __init__(
            self,
            x: int,
            next: Optional['ListNode'] = None,
    ):
        self.val: int = x
        self.next: 'ListNode' = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        forward = 0
        backward = 0
        padding = 0

        cursor = head
        while cursor is not None:
            forward += cursor.val


        i = 0
        while i < len(stack):
            if stack[i] != stack[-1]:
                return False
            stack.pop()
            i += 1

        return True


if __name__ == '__main__':
    solution = Solution()
