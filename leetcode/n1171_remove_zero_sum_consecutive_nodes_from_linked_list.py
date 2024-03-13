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
    cache,
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
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        stack_set = set()
        acc = 0
        # we need fake head in case head itself is removed
        fake_head = ListNode(val=0, next=head)

        cursor = fake_head
        while cursor is not None:
            acc += cursor.val
            if acc in stack_set:
                while stack[-1][0] != acc:
                    value = stack.pop()[0]
                    stack_set.remove(value)
            else:
                stack.append((acc, cursor))
                stack_set.add(acc)

            cursor = cursor.next

        for cursor_1, cursor_2 in zip(stack, stack[1:]):
            cursor_1[1].next = cursor_2[1]
        stack[-1][1].next = None
        return stack[0][1].next


if __name__ == '__main__':
    nodes = [
        ListNode(i)
        # for i in [1, 2, -3, 3, 1]
        # for i in [1, -1]
        for i in [1, 2, -3, 4]
    ]
    for node_1, node_2 in zip(nodes, nodes[1:]):
        node_1.next = node_2
    solution = Solution()

    result = solution.removeZeroSumSublists(head=nodes[0])
    ...
