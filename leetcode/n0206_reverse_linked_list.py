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
)


class ListNode:
    def __init__(
            self,
            x: int,
            next: Optional['ListNode'] = None,
    ):
        self.val: int = x
        self.next: 'ListNode' = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: 'TreeNode' = None,
        right: 'TreeNode' = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recurse(
        self,
        head: ListNode,
    ) -> ListNode:

        if head.next is None:
            return head

        tail = self.recurse(head=head.next)

        head.next.next = head
        head.next = None

        return tail

    def reverseList(
        self,
        head: Optional[ListNode],
    ) -> Optional[ListNode]:

        if head is None:
            return None

        return self.recurse(head=head)


if __name__ == '__main__':
    solution = Solution()
