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
    def mergeTwoLists(self, head_1: Optional[ListNode], head_2: Optional[ListNode]) -> Optional[ListNode]:
        if head_1 is None:
            return head_2
        elif head_2 is None:
            return head_1

        if head_1.val > head_2.val:
            head_1, head_2 = head_2, head_1

        cursor_1, cursor_2 = head_1, head_2
        while True:
            if (
                cursor_1 is None
                or cursor_2 is None
            ):
                return head_1

            if cursor_1.next is None:
                cursor_1.next = cursor_2
                return head_1
            elif cursor_1.next.val >= cursor_2.val:
                temp = cursor_2.next
                # do the swapping
                cursor_1.next, cursor_2.next = cursor_2, cursor_1.next
                cursor_2 = temp
                cursor_1 = cursor_1.next
            else:
                cursor_1 = cursor_1.next


if __name__ == '__main__':
    solution = Solution()
    nodes_1 = [
        ListNode(x=1),
        ListNode(x=2),
        ListNode(x=3),
        ListNode(x=4),
        # ListNode(x=5),
    ]
    for index, node in enumerate(nodes_1[:-1]):
        node.next = nodes_1[index + 1]
    nodes_2 = [
        # ListNode(x=1),
        # ListNode(x=2),
        # ListNode(x=3),
        # ListNode(x=4),
        # ListNode(x=5),
        ListNode(x=6),
    ]
    for index, node in enumerate(nodes_2[:-1]):
        node.next = nodes_2[index + 1]

    # result = solution.mergeTwoLists(head_1=None, head_2=None)
    result = solution.mergeTwoLists(head_1=nodes_1[0], head_2=nodes_2[0])
    print(result)
