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

    def twoSum(
        self,
        nums: List[int],
        target: int,
    ) -> List[int]:

        nums_dict = {}
        index_left = 0
        index_right = len(nums) - 1

        while index_left < index_right:
            current = nums[index_left] + nums[index_right]
            if current == target:
                return [index_left, index_right]
            elif current < target:
                index_left += 1
            elif current > target:
                index_right -= 1

        return []


if __name__ == '__main__':
    solution = Solution()
