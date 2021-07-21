from typing import (
    List,
)
from collections import (
    deque,
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
    zip_longest,
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

    def partition(
        self,
        head: ListNode,
        x: int,
    ) -> ListNode:

        if head is None:
            return head

        less = []
        greater_or_equal = []

        while head is not None:
            if head.val < x:
                less.append(head)
            else:
                greater_or_equal.append(head)
            head = head.next

        nodes = [
            *less,
            *greater_or_equal,
        ]
        for index in range(0, len(nodes) - 1):
            nodes[index].next = nodes[index + 1]

        nodes[-1].next = None

        return nodes[0]


def create_nodes(
    values: List[int],
    index: int,
) -> ListNode:

    if index >= len(values):
        return None
    else:
        return ListNode(
            val=values[index],
            next=create_nodes(
                values=values,
                index=index + 1,
            )
        )


def print_(
    head: ListNode,
):
    while head is not None:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    solution = Solution()
    for values, x in [
        ([1, 4, 3, 2, 5, 2], 3),
        # ([1, 1, 3, 7, 2], 3),
    ]:
        head = create_nodes(
            values=values,
            index=0,
        )
        # print_(head)
        print_(
            solution.partition(
                head=create_nodes(
                    values=values,
                    index=0,
                ),
                x=x,
            )
        )
