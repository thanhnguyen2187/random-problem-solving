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


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_maximal_position = 1
        for index, num in enumerate(nums):
            new_maximal_position = num + index + 1
            if index + 1 <= current_maximal_position:
                current_maximal_position = max(
                    current_maximal_position,
                    new_maximal_position,
                )
        return current_maximal_position > len(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.canJump(nums=[2, 3, 1, 1, 4]))
    print(solution.canJump(nums=[3, 2, 1, 0, 4]))
