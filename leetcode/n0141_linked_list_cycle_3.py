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
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False

        slow = head
        fast = head

        while True:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
            if slow is None or fast is None:
                return False
            elif slow == fast:
                return True

if __name__ == "__main__":
    solution = Solution()
    for head in [
        ListNode(x=1, next=ListNode(x=2)),
    ]:
        print(
            solution.hasCycle(
                head=head,
            )
        )
