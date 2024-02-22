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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        cursor_1 = l1
        cursor_2 = l2

        while True:
            if cursor_1 is None and cursor_2 is None:
                break
            elif cursor_1.next is not None and cursor_2.next is None:
                cursor_2.next = ListNode(0)
            elif cursor_1.next is None and cursor_2.next is not None:
                cursor_1.next = ListNode(0)

            cursor_1.val += cursor_2.val + carry
            carry = 0
            if cursor_1.val >= 10:
                carry += 1
                cursor_1.val -= 10

            cursor_1 = cursor_1.next
            cursor_2 = cursor_2.next

        # handle edge case where the carry is 1, but we finished the first pass
        if carry > 0:
            cursor_1 = l1
            while cursor_1.next is not None:
                cursor_1 = cursor_1.next
            cursor_1.next = ListNode(carry)

        return l1


if __name__ == '__main__':
    solution = Solution()
    nodes_1 = [
        ListNode(x=2),
        ListNode(x=4),
        ListNode(x=9),
    ]
    for index, node in enumerate(nodes_1[:-1]):
        node.next = nodes_1[index + 1]
    nodes_2 = [
        ListNode(x=5),
        ListNode(x=6),
        ListNode(x=4),
        ListNode(x=9),
    ]
    for index, node in enumerate(nodes_2[:-1]):
        node.next = nodes_2[index + 1]

    solution.addTwoNumbers(l1=nodes_1[0], l2=nodes_2[0])
    print()

