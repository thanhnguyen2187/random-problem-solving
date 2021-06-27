from typing import (
    List,
    Optional,
)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def next_different(
        self,
        node: ListNode,
    ) -> Optional[ListNode]:
        if (
            not (node is None) and
            not (node.next is None)
        ):
            first: ListNode = node
            second: ListNode = node.next
            if first.val != second.val:
                return second
            else:
                return self.next_different(node=second)

        return None

    def replace(
        self,
        first: ListNode,
        second: ListNode,
    ):
        if (
            not (first is None) and
            not (second is None)
        ):
            first.val = second.val
            first.next = second.next

    def delete(
        self,
        head: ListNode,
    ):
        if (
            not (head is None) and
            not (head.next is None)
        ):
            first: ListNode = head
            second: ListNode = head.next
            next_different = self.next_different(node=first)

            if second.val != next_different.val:
                self.replace(first=first, second=next_different)
            else:
                ...


    def deleteDuplicates(self, head: ListNode) -> ListNode:
        self.delete(head=head)
        return head


if __name__ == '__main__':
    solution = Solution()