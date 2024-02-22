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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cursor_left = head
        cursor_right = head
        for _ in range(n):
            cursor_right = cursor_right.next

        if cursor_right is None:
            return head.next

        while cursor_right.next is not None:
            cursor_left = cursor_left.next
            cursor_right = cursor_right.next

        cursor_left.next = cursor_left.next.next
        return head


if __name__ == '__main__':
    solution = Solution()
