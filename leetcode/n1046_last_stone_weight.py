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
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


def recurse(stones: List[int]) -> int:
    if len(stones) == 0:
        return 0
    elif len(stones) == 1:
        return stones[0]
    else:
        x, y = stones[-2:]
        return recurse(stones=sorted([*stones[:-2], (y - x)]))


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        return recurse(stones=sorted(stones))


if __name__ == '__main__':
    solution = Solution()
