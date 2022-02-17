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

    def maxSubArray(
        self,
        nums: List[int],
    ) -> int:

        result = [0]
        for num in nums:
            x = result[-1] + num
            result.append(max(x, num))

        return max(*result[1:], float("-inf"))


if __name__ == '__main__':
    solution = Solution()
    for nums in [
        [1],
    ]:
        print(
            solution.maxSubArray(nums=nums)
        )
