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
    combinations,
    permutations,
    product,
    repeat,
    takewhile,
)
from functools import (
    cached_property,
    reduce,
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

    def LIS(self, nums: List[int]) -> bool:
        result = list(repeat(1, len(nums)))
        for i, j in combinations(
            range(len(nums)),
            2,
        ):
            ...

    def increasingTriplet(self, nums: List[int]) -> bool:
        nums_with_index = [
            (index, num)
            for index, num in enumerate(nums)
        ]
        sorted_nums_with_index = sorted(nums_with_index, key=lambda pair: pair[1])
        sequence = [
            index
            for index, _ in sorted_nums_with_index
        ]

        increasing_sequence = []
        for index_1, index_2 in zip(
            sequence,
            [float("inf"), *sequence],
        ):
            if index_1 > index_2:
                increasing_sequence.append(increasing_sequence[-1] + 1)
            else:
                increasing_sequence.append(1)

        return max(increasing_sequence) >= 3


if __name__ == '__main__':
    solution = Solution()
    print(
        list(combinations(range(0, 5), 2))
    )

