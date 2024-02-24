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


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [
            (cursor.val, cursor)
            for cursor in lists
            if cursor is not None
        ]
        heapq.heapify(heap)

        result_head = None
        result_cursor = None

        while len(heap) > 0:
            value, cursor = heapq.heappop(heap)
            result_node = ListNode(value)
            if result_head is None:
                result_head = result_node
                result_cursor = result_head
            else:
                result_cursor.next = result_node
                result_cursor = result_cursor.next

            if cursor.next is None:
                continue

            cursor = cursor.next
            heapq.heappush(heap, (cursor.val, cursor))

        return result_head


if __name__ == '__main__':
    solution = Solution()
