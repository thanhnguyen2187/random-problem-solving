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


class NumArray:

    def __init__(
        self,
        nums: List[int],
    ):
        self.nums = nums
        self.nums_accumulated = list(accumulate(nums))

    def sumRange(
        self,
        left: int,
        right: int,
    ) -> int:

        return (
            self.nums_accumulated[right] -
            self.nums_accumulated[left] +
            self.nums[left]
        )


if __name__ == '__main__':
    solution = Solution()
