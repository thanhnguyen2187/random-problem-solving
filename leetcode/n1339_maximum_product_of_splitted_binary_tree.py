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
        root: Optional[TreeNode],
        encountered: Set[int],
    ) -> int:

        if root is not None:
            sum_left = self.recurse(
                root=root.left,
                encountered=encountered,
            )
            sum_right = self.recurse(
                root=root.right,
                encountered=encountered,
            )
            sum_root = root.val + sum_left + sum_right

            encountered.add(sum_left)
            encountered.add(sum_right)
            encountered.add(sum_root)

            return sum_root

        return 0

    def maxProduct(
        self,
        root: Optional[TreeNode],
    ) -> int:
        encountered = set()
        self.recurse(
            root=root,
            encountered=encountered,
        )

        result = 0
        if len(encountered) >= 2:
            tree_sum = max(encountered)
            for x in encountered:
                inverted_x = tree_sum - x
                result = max(result, inverted_x * x)

        return result % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution()
    for root in [
        TreeNode(
            val=1,
            left=TreeNode(
                val=2,
                left=TreeNode(
                    val=4,
                ),
                right=TreeNode(
                    val=5,
                ),
            ),
            right=TreeNode(
                val=3,
                left=TreeNode(
                    val=6,
                ),
            )
        ),
    ]:
        print(
            solution.maxProduct(root=root)
        )
