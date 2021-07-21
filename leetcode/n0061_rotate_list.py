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

    def rotate(
        self,
        first: ListNode,
        head: ListNode,
        k: int,
    ) -> (
        ListNode,
        int,
    ):
        if (
            head is None or
            head.next is None
        ):
            return (
                head,
                0,
            )

        node, rotated = self.rotate(
            first=first,
            head=head.next,
            k=k,
        )
        if rotated < k and node.next is not None:
            node.next.next = first.next
            first.next = node.next
            node.next = None

            return (
                head,
                rotated + 1,
            )

        return (
            head,
            rotated,
        )

    def rotateRight(
        self,
        head: ListNode,
        k: int,
    ) -> ListNode:

        if (
            # there is 0 node
            head is None or
            # there is 1 node
            head.next is None or
            # no need shuffling
            k == 0
        ):
            return head

        first = ListNode(
            val=0,
            next=head,
        )

        while k > 0:
            _, rotated = self.rotate(
                first=first,
                head=first,
                k=k,
            )
            length = rotated + 1
            k -= rotated
            k %= length

        return first.next


def print_(head: ListNode):
    while head is not None:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    solution = Solution()

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
    head = solution.rotateRight(
        head=head,
        k=10,
    )
    print_(head=head)

    head = ListNode(
        val=1,
        next=ListNode(
            val=2,
        )
    )
    head = solution.rotateRight(
        head=head,
        k=1,
    )
    print_(head=head)

