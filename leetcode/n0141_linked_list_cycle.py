from typing import (
    Optional,
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

    def hasCycle(
        self,
        head: ListNode,
    ) -> bool:

        if head is None:
            return False

        slower = head
        faster = head

        while True:
            slower = slower.next
            faster = (
                faster.next
                if faster.next is None
                else faster.next.next
            )

            if (
                slower is None or
                faster is None
            ):
                return False
            elif (
                slower is faster
            ):
                return True


if __name__ == "__main__":
    solution = Solution()
    for head in [
        ListNode(
            x=1,
            next=ListNode(
                x=2,
            )
        ),
    ]:
        print(
            solution.hasCycle(
                head=head,
            )
        )
