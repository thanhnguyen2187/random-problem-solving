from typing import (
    List,
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
        next: 'ListNode' = None,
    ):
        self.val = val
        self.next = next


class Solution:

    def reverse_n(
        self,
        head: ListNode,
        n: int,
    ) -> ListNode:

        if n == 1:
            return head

        tail = self.reverse_n(
            head=head.next,
            n=n - 1,
        )

        temp = head.next.next
        head.next.next = head
        head.next = temp

        return tail

    def reverseBetween(
        self,
        head: ListNode,
        left: int,
        right: int,
    ) -> ListNode:

        if left == 1:
            return self.reverse_n(
                head=head,
                n=right,
            )
        elif left > 1:
            first = head
            current = head
            counter = 1
            while counter < left - 1:
                current = current.next
                counter += 1
            current.next = self.reverse_n(
                head=current.next,
                n=right - left + 1,
            )
            return first



if __name__ == '__main__':
    solution = Solution()
    ...
