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
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for index in range(len(nums)):
            if index <= max_index:
                max_index = max(max_index, index + nums[index])

        return max_index >= len(nums) - 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.canJump(nums=[2, 3, 1, 1, 4]))
    print(solution.canJump(nums=[3, 2, 1, 0, 4]))
