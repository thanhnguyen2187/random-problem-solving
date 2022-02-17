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

    def fill_numbers(
        self,
        node: Optional[TreeNode],
        counter: Counter,
    ):
        if node is not None:
            counter[node.val] += 1
            self.fill_numbers(
                node=node.left,
                counter=counter,
            )
            self.fill_numbers(
                node=node.right,
                counter=counter,
            )

    def findTarget(
        self,
        root: Optional[TreeNode],
        k: int,
    ) -> bool:

        counter = Counter()
        self.fill_numbers(
            node=root,
            counter=counter,
        )

        for number, count in counter.items():
            if (
                number * 2 == k and
                count >= 2
            ):
                return True
            elif (
                number * 2 != k and
                count >= 1 and
                counter[k - number] >= 1
            ):
                return True

        return False


if __name__ == '__main__':
    solution = Solution()
    for root, k in [
        (
            TreeNode(val=1), 2,
        ),
    ]:
        print(
            solution.findTarget(
                root=root,
                k=k,
            )
        )
