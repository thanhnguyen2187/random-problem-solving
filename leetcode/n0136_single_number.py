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
    reduce,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, result: result ^ x, nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber(nums=[2, 2, 1]))
    print(solution.singleNumber(nums=[4, 2, 1, 1, 2]))
    print(solution.singleNumber(nums=[1, 1, 3]))
    print(solution.singleNumber(nums=[4, 2, 1, 1, 2]))
