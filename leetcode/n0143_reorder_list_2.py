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
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        cursor = head
        while cursor is not None:
            stack.append(cursor)
            cursor = cursor.next

        cursor = head
        while True:
            top = stack.pop()
            if (
                cursor is top
                or cursor.next is top
            ):
                top.next = None
                return

            cursor.next, top.next = top, cursor.next
            cursor = top.next



if __name__ == '__main__':
    solution = Solution()
    nodes = [
        ListNode(x=1),
        ListNode(x=2),
        ListNode(x=3),
        ListNode(x=4),
        ListNode(x=5),
        ListNode(x=6),
        ListNode(x=7),
    ]
    for index, node in enumerate(nodes[:-1]):
        node.next = nodes[index + 1]

    solution.reorderList(head=nodes[0])

    cursor = nodes[0]
    while cursor is not None:
        print(cursor.val)
        cursor = cursor.next
