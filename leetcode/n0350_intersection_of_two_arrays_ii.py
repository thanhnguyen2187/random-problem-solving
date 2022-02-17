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
    Counter,
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

    def intersect(
        self,
        nums1: List[int],
        nums2: List[int],
    ) -> List[int]:

        counter_1 = Counter(nums1)
        counter_2 = Counter(nums2)

        counter_1, counter_2 = (
            (counter_1, counter_2)
            if len(nums1) < len(nums2)
            else (counter_2, counter_1)
        )

        result = []
        for key, value in counter_1.items():
            x = min(counter_2[key], value)
            result.extend([key] * x)

        return result



if __name__ == '__main__':
    solution = Solution()
