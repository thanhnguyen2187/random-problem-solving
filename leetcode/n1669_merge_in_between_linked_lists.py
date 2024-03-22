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
        x: int,
        next: Optional['ListNode'] = None,
    ):
        self.val: int = x
        self.next: 'ListNode' = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cursor = list1

        # We can traverse without checking for `None` because the description
        # stated that:
        #
        #   1 <= a <= b < list1.length - 1
        for i in range(a - 2):
            cursor = cursor.next
        temp = cursor
        for i in range(a, b + 2):
            cursor = cursor.next

        last = list2
        while last.next is not None:
            last = last.next

        temp.next = list2
        last.next = cursor

        return list1


if __name__ == '__main__':
    solution = Solution()
    nodes_1 = [
        ListNode(x)
        for x in range(7)
    ]
    nodes_2 = [
        ListNode(x)
        for x in [10, 11, 12]
    ]
    for node_1, node_2 in zip(nodes_1, nodes_1[1:]):
        node_1.next = node_2
    for node_1, node_2 in zip(nodes_2, nodes_2[1:]):
        node_1.next = node_2

    result = solution.mergeInBetween(list1=nodes_1[0], list2=nodes_2[0], a=3, b=4)
    ...
