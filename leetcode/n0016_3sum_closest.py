from typing import (
    List,
    Optional,
    Union,
    NamedTuple,
    Dict,
    Set,
    Iterator,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    product,
    cycle,
    repeat,
    islice,
    chain,
    accumulate,
    takewhile,
    permutations,
)
from functools import (
    cached_property,
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

    def threeSumClosest(
        self,
        nums: List[int],
        target: int,
    ) -> int:

        nums.sort()
        n = len(nums)
        three_sum_closest = float("-inf")

        for index_middle in range(1, n - 1):
            index_left = index_middle - 1
            index_right = index_middle + 1
            while True:
                if (
                    index_left < 0 or
                    index_right >= n
                ):
                    break
                three_sum_current = sum(
                    (
                        nums[index_left],
                        nums[index_middle],
                        nums[index_right],
                    )
                )
                three_sum_closest = min(
                    three_sum_current,
                    three_sum_closest,
                    key=lambda x: abs(x - target),
                )
                if three_sum_current > target:
                    index_left -= 1
                else:
                    index_right += 1

        return three_sum_closest


if __name__ == '__main__':
    solution = Solution()
    for nums, target in [
        ([-1, 2, 1, -4], 1),
    ]:
        print(
            solution.threeSumClosest(
                nums=nums,
                target=target,
            )
        )
