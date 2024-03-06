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
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        return ((n * (n - 1)) // 2) - sum(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.missingNumber(nums=[3, 0, 1]))
