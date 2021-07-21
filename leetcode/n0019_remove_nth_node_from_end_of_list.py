from typing import (
    List,
    Optional,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    product,
    accumulate,
    takewhile,
    islice,
    chain,
    cycle,
    repeat,
)


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next: Optional['ListNode'] = None,
    ):
        self.val = val
        self.next = next


class Solution:

    def remove_nth(
        self,
        head: ListNode,
        n: int,
    ) -> (
        ListNode,
        int,
    ):

        if head.next is None:
            return (
                head,
                1,
            )

        node, position = self.remove_nth(
            head=head.next,
            n=n,
        )
        if position == n + 1:
            node.next = node.next.next

        return (
            head,
            position + 1,
        )

    def removeNthFromEnd(
        self,
        head: ListNode,
        n: int,
    ) -> ListNode:
        first = ListNode(
            next=head,
        )
        _, position = self.remove_nth(
            head=first,
            n=n,
        )

        if position == n + 1:
            first.next = first.next.next

        return first.next


def print_(head: ListNode):
    while head is not None:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    head = ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=3,
                next=ListNode(
                    val=4,
                    next=ListNode(
                        val=5,
                        next=None,
                    )
                )
            )
        )
    )

    solution = Solution()
    solution.removeNthFromEnd(
        head=head,
        n=5,
    )

    print_(head=head)
