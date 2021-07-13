from typing import (
    List,
)


class ListNode:
    def __init__(
        self,
        val: int =0,
        next: 'ListNode' = None,
    ):
        self.val = val
        self.next = next


class Solution:

    def remove_nth(
        self,
        first: ListNode,
        head: ListNode,
        n: int,
        counter: int,
    ) -> ListNode:

        if not head.next is None:
            self.remove_nth(
                first=first,
                head=head.next,
                n=n,
                counter=counter + 1,
            )

        return first.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ...


if __name__ == '__main__':
    ...
