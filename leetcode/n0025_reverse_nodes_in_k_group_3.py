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
        val: int,
        next: Optional['ListNode'] = None,
    ):
        self.val: int = val
        self.next: 'ListNode' = next


def reverse_until(fake_head: Optional[ListNode], last: ListNode):
    stack = []
    cursor = fake_head.next
    last_next = last.next

    while cursor != last:
        stack.append(cursor)
        cursor = cursor.next
    stack.append(last)

    cursor = fake_head
    while len(stack) > 0:
        cursor.next = stack.pop()
        cursor = cursor.next

    cursor.next = last_next

    return cursor


def next_k_nodes(cursor: ListNode, k: int) -> Optional[ListNode]:
    for _ in range(k):
        cursor = (
            cursor.next
            if cursor is not None
            else None
        )

    return cursor


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        correct_head = next_k_nodes(cursor=head, k=k - 1)
        fake_head = ListNode(val=-1, next=head)

        while True:
            last = next_k_nodes(cursor=fake_head, k=k)
            if last is None:
                return (
                    correct_head
                    if correct_head is not None
                    else head
                )

            last = reverse_until(fake_head=fake_head, last=last)
            fake_head = last


if __name__ == '__main__':
    solution = Solution()
    nodes = [
        ListNode(value)
        for value in range(0, 6)
    ]
    for node_1, node_2 in zip(nodes, nodes[1:]):
        node_1.next = node_2

    solution.reverseKGroup(head=nodes[0], k=3)
    print()
