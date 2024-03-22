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
        val: int,
        next: Optional['ListNode'] = None,
    ):
        self.val: int = val
        self.next: 'ListNode' = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        fake_head = ListNode(val=-1, next=head)
        last = None

        def recurse(head: Optional[ListNode]):
            if head is None or head.next is None:
                nonlocal last
                last = head
                return

            recurse(head=head.next)
            head.next.next = head

        recurse(head=fake_head.next)
        fake_head.next.next = None

        return last


if __name__ == '__main__':
    solution = Solution()
    nodes = [
        # ListNode(val=1),
        # ListNode(val=2),
        # ListNode(val=3),
        # ListNode(val=4),
        # ListNode(val=5),
    ]
    for index, node in enumerate(nodes[:-1]):
        node.next = nodes[index + 1]

    # result = solution.reverseList(head=nodes[0])
    result = solution.reverseList(None)
    print(result)
