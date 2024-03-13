import heapq

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

    def __lt__(self, other):
        return self.val < other.val


def merge_2(list_1: Optional[ListNode], list_2: Optional[ListNode]) -> Optional[ListNode]:
    match list_1, list_2:
        case None, None:
            return None
        case _, None:
            return list_1
        case None, _:
            return list_2

    if list_1.val > list_2.val:
        list_1, list_2 = list_2, list_1

    cursor_1 = list_1
    cursor_2 = list_2
    while True:
        if cursor_1.next is None:
            cursor_1.next = cursor_2
            return list_1
        if cursor_2 is None:
            return list_1

        if cursor_1.val <= cursor_2.val <= cursor_1.next.val:
            temp = cursor_2.next
            cursor_1.next, cursor_2.next = cursor_2, cursor_1.next
            cursor_2 = temp
        else:
            cursor_1 = cursor_1.next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]

        dq = deque(lists)
        while len(dq) > 1:
            list_1, list_2 = dq.popleft(), dq.popleft()
            dq.append(merge_2(list_1=list_1, list_2=list_2))

        return dq[0]


if __name__ == '__main__':
    solution = Solution()
