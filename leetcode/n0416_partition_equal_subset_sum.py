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
    combinations,
    cycle,
    islice,
    permutations,
    product,
    repeat,
    takewhile,
)
from functools import (
    cache,
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False

        req = sum_ // 2
        @cache
        def recurse(i: int, current: int):
            if current == req:
                return True

            if current > req or i >= len(nums):
                return False
            num = nums[i]
            return (
                recurse(i=i + 1, current=current + num) or
                recurse(i=i + 1, current=current)
            )

        return recurse(i=0, current=0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.canPartition(nums=[1, 2, 2, 5, 1]))
