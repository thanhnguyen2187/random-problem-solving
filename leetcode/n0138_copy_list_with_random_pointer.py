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


class Node:
    def __init__(
        self,
        x: int,
        next: Optional['Node'] = None,
        random: Optional['Node'] = None,
    ):
        self.val: int = x
        self.next: Optional['Node'] = next
        self.random: Optional['Node'] = random
        self.equivalent: Optional['Node'] = None


def clone(head: 'Optional[Node]') -> 'Optional[Node]':
    if head is None:
        return

    cloned_head = Node(head.val)
    head.equivalent = cloned_head
    cloned_head.random = head.random

    cursor_head = head.next
    cursor_clone = cloned_head
    while cursor_head is not None:
        cursor_clone.next = Node(cursor_head.val)
        cursor_clone = cursor_clone.next
        cursor_head.equivalent = cursor_clone
        cursor_clone.random = cursor_head.random
        cursor_head = cursor_head.next

    return cloned_head


def fix_random_references(cloned_head: 'Optional[Node]') -> 'Optional[Node]':
    cursor = cloned_head
    while cursor is not None:
        if cursor.random is not None:
            cursor.random = cursor.random.equivalent
        cursor = cursor.next


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cloned_head = clone(head=head)
        fix_random_references(cloned_head=cloned_head)

        return cloned_head


if __name__ == '__main__':
    solution = Solution()
    nodes = [
        Node(x=0),
        Node(x=1),
        Node(x=2),
        Node(x=3),
        Node(x=4),
        Node(x=5),
        Node(x=6),
    ]
    for index, node in enumerate(nodes[:-1]):
        node.next = nodes[index + 1]

    nodes[0].random = nodes[3]
    nodes[1].random = nodes[2]
    nodes[2].random = nodes[6]
    nodes[3].random = nodes[0]
    nodes[4].random = nodes[0]
    nodes[5].random = nodes[1]

    cloned_node = clone(head=nodes[0])
    fix_random_references(cloned_head=cloned_node)

    print(cloned_node)
