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

        nums_indexed = [
            (number, index)
            for index, number in enumerate(nums)
        ]
        nums_indexed.sort()
        index_left = 0
        index_right = len(nums) - 1

        while index_left < index_right:
            current = nums_indexed[index_left][0] + nums_indexed[index_right][0]
            if current < target:
                index_left += 1
            elif current > target:
                index_right -= 1
            else:
                return [
                    nums_indexed[index_left][1],
                    nums_indexed[index_right][1],
                ]


if __name__ == '__main__':
    solution = Solution()

    for nums, target in [
        # ([2, 7, 11, 15], 9,),
        # ([3, 2, 4], 6,),
        ([3, 3], 6,),
    ]:
        print(
            solution.twoSum(
                nums=nums,
                target=target,
            )
        )
