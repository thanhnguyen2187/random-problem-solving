from typing import (
    List,
)


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next: 'ListNode' = None,
    ):
        self.val = val
        self.next = next


class Solution:

    def reorder(
        self,
        head: ListNode,
    ) -> ListNode:

        if (
            head.next is None
        ):
            return head

        node = self.reorder(head=head.next)

        node_second = node.next
        node_third = (
            node_second.next
            if node_second is not None
            else None
        )
        if (
            node_second is not None and
            node_third is not None
        ):
            node.next = node_third
            node_second.next = node_third.next
            node_third.next = node_second

        return node

    def reorderList(self, head: ListNode) -> None:

        while (
            head is not None
        ):
            self.reorder(
                head=head,
            )
            node_second = head.next
            node_third = (
                node_second.next
                if node_second is not None
                else None
            )
            head = node_third

