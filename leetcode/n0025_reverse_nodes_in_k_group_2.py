"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up
- Could you solve the problem in O(1) extra memory space?
- You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

from typing import (
    Optional,
)


class ListNode:
    # Definition for singly-linked list.
    def __init__(
        self,
        val: int = 0,
        next: 'ListNode' = None,
    ):
        self.val = val
        self.next = next


class Solution:

    def reverse_k(
        self,
        head: ListNode,
        k: int,
        remains: int,
        # counter: int,
    ) -> (
        ListNode,
        bool,
    ):

        if (
            head is not None and
            head.next is None
        ):
            return head, remains == 1
        elif (
            remains == 1
        ):
            head.next, _ = self.reverse_k(
                head=head.next,
                k=k,
                remains=k,
            )
            return head, True

        tail, allowed = self.reverse_k(
            head=head.next,
            k=k,
            remains=remains - 1,
        )
        if allowed:
            temp = head.next.next
            head.next.next = head
            head.next = temp
        else:
            # print(head.val)
            return head, False

        return tail, allowed

    def reverseKGroup(
        self,
        head: ListNode,
        k: int,
    ) -> ListNode:

        head, _ = self.reverse_k(
            head=head,
            k=k,
            remains=k,
        )
        return head


def print_(head: ListNode):
    while head is not None:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    solution = Solution()
    for head, k in [
        (
            ListNode(
                val=1,
                next=ListNode(
                    val=2,
                    next=ListNode(
                        val=3,
                        next=ListNode(
                            val=4,
                            next=ListNode(
                                val=5,
                                next=ListNode(
                                    val=6,
                                    next=ListNode(
                                        val=7,
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ), 3
        ),
        (
            ListNode(
                val=1,
                next=ListNode(
                    val=2,
                )
            ), 2
        )
    ][1:]:
        head = solution.reverseKGroup(
            head=head,
            k=k,
        )
        # print(head)
        print_(head=head)
