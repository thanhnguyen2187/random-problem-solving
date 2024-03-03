import bisect

import heapq

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


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        bisect.insort(self.heap, val)
        return self.heap[len(self.heap) - self.k]


if __name__ == '__main__':
    solution = Solution()
