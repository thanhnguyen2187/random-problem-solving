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

    def arrayNesting(
        self,
        nums: List[int],
    ) -> int:

        traversed = [
            False
            for _ in nums
        ]

        def traverse(index: int):
            if not traversed[index]:
                traversed[index] = True
                return 1 + traverse(nums[index])

            return 0

        return max(
            traverse(index=index)
            for index in range(len(nums))
        )


if __name__ == '__main__':
    solution = Solution()
    for nums in [
        [1, 3, 4, 2, 5, 0],
        [5, 4, 0, 3, 1, 6, 2],
    ]:
        print(
            solution.arrayNesting(nums=nums)
        )
