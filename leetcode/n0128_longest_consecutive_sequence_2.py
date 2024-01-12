from typing import (
    DefaultDict,
    Dict,
    Iterator,
    List,
    NamedTuple,
    Optional,
    Set,
    FrozenSet,
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


@cache
def recurse(num: int, nums_set: FrozenSet):
    num_inc = num + 1
    if num_inc in nums_set:
        return 1 + recurse(num=num_inc, nums_set=nums_set)

    return 1


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = frozenset(nums)
        for n in nums_set:
            if n - 1 not in nums_set:
                i = 1
                while n + i in nums_set:
                    i += 1
                longest = max(longest, i)
        return longest


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
