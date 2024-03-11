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
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        match list1, list2:
            case (None, _):
                return list2
            case (_, None):
                return list1
            case (None, None):
                return None

        if list1.val > list2.val:
            list1, list2 = list2, list1

        cursor_1, cursor_2 = list1, list2
        while True:
            if cursor_2 is None:
                return list1
            if cursor_1.next is None:
                cursor_1.next = cursor_2
                return list1

            if cursor_1.val <= cursor_2.val <= cursor_1.next.val:
                # store the relevant reference
                temp = cursor_2.next
                # do the "insertion"
                cursor_1.next, cursor_2.next = cursor_2, cursor_1.next
                # advance `cursor_2`
                cursor_2 = temp
            else:
                cursor_1 = cursor_1.next



if __name__ == '__main__':
    solution = Solution()
    nodes_1 = [
        ListNode(x=i)
        for i in [-9, -7, -3, -3, -1, 2, 3]
    ]
    for node_1, node_2 in zip(nodes_1, nodes_1[1:]):
        node_1.next = node_2
    nodes_2 = [
        ListNode(x=i)
        for i in [-7,-7,-6,-6,-5,-3,2,4]
    ]
    for node_1, node_2 in zip(nodes_2, nodes_2[1:]):
        node_1.next = node_2

    result = solution.mergeTwoLists(list1=nodes_1[0], list2=nodes_2[0])
    ...
