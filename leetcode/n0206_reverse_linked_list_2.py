from typing import (
    DefaultDict,
    Dict,
    Iterator,
    List,
    NamedTuple,
    Optional,
    Set,
    Union,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    accumulate,
    chain,
    combinations,
    cycle,
    islice,
    permutations,
    product,
    repeat,
    takewhile,
)
from functools import (
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        last = head
        while last is not None and last.next is not None:
            last = last.next

        def recurse(head: Optional[ListNode]):
            if head is None or head.next is None:
                return

            recurse(head=head.next)
            head.next.next = head

        recurse(head=head)
        if head is not None:
            head.next = None

        return last


if __name__ == '__main__':
    solution = Solution()
    nodes = [
        ListNode(x=1),
        ListNode(x=2),
        ListNode(x=3),
        ListNode(x=4),
        ListNode(x=5),
    ]
    for index, node in enumerate(nodes[:-1]):
        node.next = nodes[index + 1]

    result = solution.reverseList(head=nodes[0])
    print(result)
